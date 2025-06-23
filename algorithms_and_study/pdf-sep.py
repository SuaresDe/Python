#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path: str, output_folder: str):
    """
    Separa cada página do PDF de entrada em um arquivo próprio.

    :param input_pdf_path: caminho para o arquivo PDF de origem
    :param output_folder: pasta onde os PDFs individuais serão salvos
    """
    reader = PdfReader(input_pdf_path)
    num_pages = len(reader.pages)

    os.makedirs(output_folder, exist_ok=True)

    for i, page in enumerate(reader.pages, start=1):
        writer = PdfWriter()
        writer.add_page(page)

        output_filename = f"page_{i:03d}.pdf"
        output_path = os.path.join(output_folder, output_filename)

        with open(output_path, "wb") as out_f:
            writer.write(out_f)

        print(f"[OK] Página {i}/{num_pages} → {output_filename}")

    print(f"\nConcluído! {num_pages} arquivos gerados em '{output_folder}'.")


def main():
    # Diretório atual
    cwd = os.getcwd()

    # Pergunta pelo nome do arquivo
    input_pdf = input("Digite o nome do arquivo PDF (deve estar na mesma pasta que este script): ").strip()

    # Verifica se o arquivo existe no diretório atual
    input_path = os.path.join(cwd, input_pdf)
    if not os.path.isfile(input_path):
        print(f"❌ Arquivo '{input_pdf}' não encontrado em:\n   {cwd}")
        sys.exit(1)

    # Define a pasta de saída automaticamente
    base_name, _ = os.path.splitext(input_pdf)
    output_folder = f"{base_name}_pages"

    split_pdf(input_path, output_folder)


if __name__ == "__main__":
    main()
