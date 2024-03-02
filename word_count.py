"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #
    filenames = glob.glob(f'{input_directory}\*.txt')
    dfs = [
        pd.read_csv(filename, sep='\t', header=None, names=['text']) for filename in filenames
    ]
    
    concatenated_df = pd.concat(dfs, ignore_index=True)
    return concatenated_df
    

def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    dataframe = dataframe.copy()
    dataframe['text'] = dataframe.text.str.lower().str.replace('.','').str.replace(',','')
    return dataframe


# def count_words(dataframe):
#     """Word count"""
    
#     dataframe = dataframe.copy()
#     dataframe['text'] = dataframe.text.str.split()
#     dataframe = dataframe.explode('text')
#     dataframe['count'] = 1
#     return dataframe.groupby(['text'], as_index=False)[['count']].sum().sort_values('count', ascending=False)


def count_words2(dataframe):
    """Word count"""
    
    dataframe = dataframe.copy()
    dataframe['text'] = dataframe.text.str.split()
    return dataframe.explode('text').text.value_counts()


def save_output(dataframe, output_filename):
    """Save output to a file."""
    dataframe.to_csv(output_filename, sep='\t', index=True, header=None)
    
#
# Escriba la función job, la cual orquesta las funciones anteriores.
#

def run(input_directory, output_filename):
    """Call all functions."""
    
    df = load_input(input_directory)
    df = clean_text(df)
    df = count_words2(df)
    save_output(df, output_filename)

if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
