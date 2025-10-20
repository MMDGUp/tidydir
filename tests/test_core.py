import os
import tempfile
from pathlib import Path
from tidydir.core import organize_directory


def test_moves_image_to_images():
    with tempfile.TemporaryDirectory() as tmpdir:
        test_file = Path(tmpdir) / "test.jpg"
        test_file.write_text("fake image")

        organize_directory(tmpdir, dry_run=False)

        assert (Path(tmpdir) / "Images" / "test.jpg").exists()
        assert not test_file.exists()