from fastapi import FastAPI, File, UploadFile
import os
import subprocess

app = FastAPI()

@app.post("/separate")
async def separate(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    input_path = f"temp/uploads/{file.filename}"
    output_dir = f"temp/output/{file.filename}_stems"
    os.makedirs(os.path.dirname(input_path), exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Run spleeter (2 stems: vocals + accompaniment)
    subprocess.run([
        "spleeter", "separate",
        "-p", "spleeter:2stems",
        "-o", output_dir,
        input_path
    ])

    return {"message": "Separation complete", "output_dir": output_dir}
