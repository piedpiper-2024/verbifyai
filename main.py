import tempfile
import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException, Response
from deployment.speech_inference import SpeechTranscriptionPipeline, ModelOptimization
from fastapi.responses import FileResponse, JSONResponse, Response

app = FastAPI(debug=True)

model_name = "openai/whisper-tiny"   # e.g., "KevinKibe/whisper-small-af"
huggingface_read_token = "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"
task = "transcribe"     
                                    # either 'translate' or 'transcribe'
model_optimizer = ModelOptimization(model_name=model_name)
model_optimizer.convert_model_to_optimized_format()
model = model_optimizer.load_transcription_model()


@app.post("/piedpiper")
async def speech_recognition(file: UploadFile):

    try:
        # Create a temporary file for the upload
        with tempfile.NamedTemporaryFile(suffix=".tmp", delete=False) as tmp_file:
            tmp_file.write(await file.read())
            tmp_file_path = tmp_file.name

        # Initiate the transcription model
        inference = SpeechTranscriptionPipeline(
                audio_file_path=tmp_file_path,
                task=task,
                huggingface_read_token=huggingface_read_token
            )

        # To get transcriptions
        transcription = inference.transcribe_audio(model=model)

        return JSONResponse(content={"transcription": transcription})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error transcribing audio: {e}")

@app.get("/")
async def health_check() -> str:
    """
    Basic health check endpoint to confirm the application is running.

    Returns:
    - str: A simple message indicating that the application is running successfully.
    """
    return "Running Successfully"

