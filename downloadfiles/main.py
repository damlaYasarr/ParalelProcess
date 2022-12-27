import sys, os
import zipfile
import requests
from multiprocessing import Pool, cpu_count
from functools import partial
from io import BytesIO


def download_zip(url, filePath):
    try:
        file_name = url.split("/")[-1]
        response = requests.get(url)
        # provide zip content
        sourceZip = zipfile.ZipFile(BytesIO(response.content))
        print(" Downloaded {} ".format(file_name))
        #provide extract data
        sourceZip.extractall(filePath)
        print(" extracted {}".format(file_name))
        sourceZip.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # provide to get computers file path, very useable item.
    filePath = os.path.dirname(os.path.abspath(__file__))
    print("filePath is %s " % filePath)
    
    urls = ["http://mlg.ucd.ie/files/datasets/multiview_data_20130124.zip",
            "http://mlg.ucd.ie/files/datasets/movielists_20130821.zip",
            "http://mlg.ucd.ie/files/datasets/bbcsport.zip",
            "http://mlg.ucd.ie/files/datasets/movielists_20130821.zip",
            "http://mlg.ucd.ie/files/datasets/3sources.zip"]

    print("There are {} CPUs on this machine ".format(cpu_count()))
    #here provide download as a parallel
    pool = Pool(cpu_count())
    #partial function
    download_func = partial(download_zip, filePath = filePath)
    #map function, url is parameter and combine them
    results = pool.map(download_func, urls)
    pool.close()
    pool.join()