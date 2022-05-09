# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    df = pd.read_csv('../data/raw/data.csv', index_col=0)
    
    df.drop('_id', axis=1, inplace=True)
    
    df.Tags = df.Tags.apply(lambda x: ', '.join(x.strip('[]\'').split("', '")))
    
    rating = {'Overwhelmingly Positive': 8, 'Very Positive': 4, 'Positive': 2,
          'Mostly Positive': 1, 'Mixed': 0, 'Mostly Negative': -1, 'Negative': -2}
    
    df.Review = df.Review.apply(lambda x: x.strip('[]\'').split("', '")[0]).map(rating)
    
    df.to_csv(output_filename)

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
