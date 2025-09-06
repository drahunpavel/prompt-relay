export interface TranscribeResult {
  text: string;
  language?: string;
  waw_duration?: number;
  transcribe_duration?: number;
}

const MAX_FILE_BYTES = 15 * 1024 * 1024; // 15 MB

export async function transcribeAudio(file: File): Promise<TranscribeResult> {
  if (file.size > MAX_FILE_BYTES) {
    throw new Error("File is too large - max 15MB");
  }

  const formData = new FormData();
  formData.append("audio", file, file.name);

  const res = await fetch(`/api/asr/transcribe`, {
    method: "POST",
    body: formData,
  });
  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(text || `HTTP ${res.status}`);
  }

  const data = await res.json();
  return {
    text: String(data?.text ?? ""),
    language: data?.language,
    waw_duration: data?.waw_duration,
    transcribe_duration: data?.transcribe_duration,
  };
}
