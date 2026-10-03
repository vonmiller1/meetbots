import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

from audio_to_text import audio_to_text
from classify_meeting import classify_meeting
from extract_audio import extract_audio_from_video
from plan_of_action import generate_plan_of_action
from sentiment_analysis import analyze_sentiment
from speaker_identification import perform_speaker_diarization
from text_summarization import summarize_text
from tone_analysis import analyze_tone


class MeetingHelperTests(unittest.TestCase):
    def test_classification_is_case_insensitive(self):
        self.assertEqual(classify_meeting("CLIENT project update"), "Client Meeting")
        self.assertEqual(classify_meeting("TEAM discussion"), "Group Discussion")

    def test_tone_detection_is_case_insensitive(self):
        self.assertEqual(analyze_tone("This is URGENT"), "Fast-paced and urgent")
        self.assertEqual(analyze_tone("Team MEETING"), "Professional")

    def test_action_plan_skips_empty_items(self):
        self.assertEqual(
            generate_plan_of_action("Review the draft. Assign an owner."),
            "- Review the draft\n- Assign an owner",
        )
        self.assertEqual(generate_plan_of_action("..."), "")

    def test_empty_nlp_inputs_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "empty text"):
            summarize_text(" \n ")
        with self.assertRaisesRegex(ValueError, "empty text"):
            analyze_sentiment("")

    def test_short_transcript_uses_valid_summary_length_limits(self):
        summarizer = Mock(return_value=[{"summary_text": "Short summary."}])
        transformers = SimpleNamespace(pipeline=Mock(return_value=summarizer))
        with patch.dict("sys.modules", {"transformers": transformers}):
            result = summarize_text("A very short meeting")

        self.assertEqual(result, "Short summary.")
        limits = summarizer.call_args.kwargs
        self.assertLessEqual(limits["min_length"], limits["max_length"])
        self.assertTrue(limits["truncation"])

    def test_audio_utilities_reject_missing_files_before_loading_dependencies(self):
        missing_file = Path(tempfile.gettempdir()) / "meetsummarizer-missing-input.wav"
        with self.assertRaises(FileNotFoundError):
            audio_to_text(missing_file)
        with self.assertRaises(FileNotFoundError):
            extract_audio_from_video(missing_file, "output.wav")
        with self.assertRaises(FileNotFoundError):
            perform_speaker_diarization(missing_file)


if __name__ == "__main__":
    unittest.main()
