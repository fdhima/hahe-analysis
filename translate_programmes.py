import pandas as pd
from googletrans import Translator
import argparse

def translate_column(input_file, output_file, column_name):
    # Initialize translator
    translator = Translator()

    # Read CSV
    df = pd.read_csv(input_file)

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in CSV. Available columns: {list(df.columns)}")

    # Translate each cell in the column
    translations = []
    print(f"Translating column '{column_name}' from Greek to English...")

    for text in df[column_name].astype(str):
        if pd.isna(text) or text.strip() == "":
            translations.append(text)
            continue
        try:
            translated_text = translator.translate(text, src='el', dest='en').text
            translations.append(translated_text)
        except Exception as e:
            print(f"⚠️ Error translating '{text}': {e}")
            translations.append(text)

    # Add translated column to DataFrame
    df[f"{column_name}_english"] = translations

    # Save new CSV
    df.to_csv(output_file, index=False)
    print(f"✅ Translation complete! Saved to '{output_file}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate a CSV column from Greek to English.")
    parser.add_argument("input", help="Path to the input CSV file.")
    parser.add_argument("output", help="Path to save the translated CSV file.")
    parser.add_argument("column", help="Name of the column to translate.")

    args = parser.parse_args()

    translate_column(args.input, args.output, args.column)
