from magic_pdf.pipe.UNIPipe import UNIPipe
from magic_pdf.rw.DiskReaderWriter import DiskReaderWriter

pipe = UNIPipe(device="cpu")  # ou "cuda"
reader = DiskReaderWriter(input_path="documento.pdf")
writer = DiskReaderWriter(output_path="./saida")

result = pipe(reader, writer)
print("Extração concluída!")