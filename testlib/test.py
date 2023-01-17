import epub_meta
import io

file = open("./testlib/Metamorphosis.epub", "rb")

with io.BytesIO(file.read()) as f:
  meta = epub_meta.get_epub_metadata(f)
  print(str(meta))  