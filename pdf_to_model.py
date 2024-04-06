import os
import glob
from pdfminer.high_level import extract_text
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
import re
import sys

def get_page_count(pdf_path: str) -> int:
    """
    ページ数取得
    Args
        pdf_path (str): ファイルパス
    Return
        page_count (int): ページ数
    """
    # PDFファイルを開く
    with open(pdf_path, 'rb') as file:
        # PDFパーサーとドキュメントオブジェクトを作成
        parser = PDFParser(file)
        document = PDFDocument(parser)
        
        # PDFPage.create_pages()を使用してページのリストを取得し、その長さを数える
        page_count = len(list(PDFPage.create_pages(document)))
        
        return page_count

def remove_whitespaces(text: str, page_count: int) -> str:
    """
    ページ番号の削除
    空白の削除
    Args
        text (str): 抽出したテキスト
        page_count (int): ページ数
    Return
        text (str): 空白削除後のテキスト
    """
    # ページ番号の削除(例：- 1 -)
    for i in range(1, page_count+1):
        text = text.replace('- ' + str(i) + ' -', '')
    # スペース、タブ、改行を削除
    text = text.replace(' ', '').replace('\t', '').replace('\n', '')

    # 正規表現を使って他の空白文字を削除
    text = re.sub(r'\s+', '', text)

    return text

# 現在のディレクトリ取得
dirname = os.getcwd()
# pdf出力用フォルダ
output_pdf = dirname + '/output_pdf'
#入力ファイル取得
file_path_list = glob.glob(output_pdf+'/*.pdf')

for pdf_path in file_path_list:
    # テスト用pdfファイル
    # pdf_path = 'output_pdf/archive/038630_hanrei.pdf'
    # print(pdf_path)
    # PDFファイルからテキスト抽出
    texts = extract_text(pdf_path)
    # print(texts)
    print('--------------------------------------------------')
    # ページ数取得
    page_count = get_page_count(pdf_path)
    # print(page_count)
    print('--------------------------------------------------')
    # ページ番号と空白削除
    rem_spe_texts = remove_whitespaces(texts, page_count)
    print(rem_spe_texts)

    sys.exit(1)
