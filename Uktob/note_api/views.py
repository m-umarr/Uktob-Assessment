import textwrap
import os

from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from .models import Note
from .serial import NoteSerializer
from rest_framework.response import Response
from rest_framework import status
# LangChain imports
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate


class SummarizeTextView(APIView):
    def get(self, request, notes_id, *args, **kwargs):
        try:
            input_text = NoteSerializer(Note.objects.get(id=notes_id)).data['content']
            if input_text:
                # Define prompt
                # doc = Document(page_content=input_text, metadata={"source": "local"})

                prompt_template = """Write a concise summary of the following:
                "{text}"
                CONCISE SUMMARY:"""
                prompt_template = PromptTemplate(template=prompt_template,
                                                 input_variables=["text"])

                # Define the LLM
                llm_key = os.environ.get("OPENAI_API_KEY")
                llm = OpenAI(api_key=llm_key, temperature=0)

                # Generating the document summary
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt_template)
                text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
                pages = text_splitter.split_text(input_text)

                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
                input_text = text_splitter.create_documents(pages)

                summarized_text = chain.run(input_text)
                summarized_text = textwrap.fill(summarized_text,
                                                width=100,
                                                break_long_words=False,
                                                replace_whitespace=False)

                return Response({"summarized_text": summarized_text}, status=status.HTTP_200_OK)
            return Response(f"This Note ID: {notes_id} does not have any content!!!", status=200)
        except Exception as e:
            return Response(str(e), status=500)


@api_view(['POST'])
def post_note(request):
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_note(request, id):
    try:
        note = Note.objects.get(pk=id)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")

    serializer = NoteSerializer(note)
    return Response(serializer.data)


@api_view(['PUT'])
def put_note(request, id):
    try:
        note = Note.objects.get(pk=id)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")

    serializer = NoteSerializer(note, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def patch_note(request, id):
    try:
        note = Note.objects.get(pk=id)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")

    serializer = NoteSerializer(note, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_note(request, id):
    try:
        note = Note.objects.get(pk=id)
    except Note.DoesNotExist:
        return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        note.delete()
        return Response({'message': 'Note deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


