import { useRef, useState } from "react";
import { useAppDispatch } from "@/store";
import { sendAudioThunk } from "./chatSlice";

const MAX_BYTES = 15 * 1024 * 1024;

export default function AudioRecorder() {
  const dispatch = useAppDispatch();
  const fileInput = useRef<HTMLInputElement>(null);
  const [recording, setRecording] = useState(false);
  const mediaRecorder = useRef<MediaRecorder | null>(null);
  const chunks = useRef<Blob[]>([]);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder.current = new MediaRecorder(stream);
    mediaRecorder.current.ondataavailable = (e) => chunks.current.push(e.data);
    mediaRecorder.current.onstop = () => {
      const blob = new Blob(chunks.current, { type: "audio/wav" });
      chunks.current = [];
      if (blob.size > MAX_BYTES) {
        alert("File is too large - max 15MB");
        return;
      }
      const file = new File([blob], "recording.wav", { type: "audio/wav" });
      dispatch(sendAudioThunk(file));
    };
    mediaRecorder.current.start();
    setRecording(true);
  };

  const stopRecording = () => {
    mediaRecorder.current?.stop();
    setRecording(false);
  };

  const pickFile = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    if (file.size > MAX_BYTES) return alert("File is too large - max 15MB");
    dispatch(sendAudioThunk(file));
  };

  return (
    <div>
      <button
        onClick={recording ? stopRecording : startRecording}
        className="px-3 py-2 bg-green-500 text-white rounded"
      >
        {recording ? "Stop" : "Record"}
      </button>
      <input
        ref={fileInput}
        type="file"
        accept="audio/*"
        hidden
        onChange={pickFile}
      />
      <button
        className="ml-2 px-3 py-2 bg-gray-300 rounded"
        onClick={() => fileInput.current?.click()}
      >
        Download audio
      </button>
    </div>
  );
}
