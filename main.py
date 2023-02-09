import pandas as pd
import glob
import os

def load_data():
    files = [i for i in glob.glob('./youtube_data/*.csv'.format('csv'))]

    all_dataframes = list()
    for csv in files:
        
        frame = pd.read_csv(csv,index_col=0)
        frame['country'] = os.path.basename(csv)
        all_dataframes.append(frame)

    combined_data = pd.concat(all_dataframes)
    combined_data['country']=combined_data['country'].map(lambda x: x.lstrip('+-').rstrip('videos.csv'))
    

    combined_data['category_id'] = combined_data['category_id'].astype(str)
    js_files = [i for i in glob.glob('./youtube_data/*.json')]
    sorted(js_files)

    id_to_category = {}
    for x in js_files:
        js = pd.read_json(x)
        for category in js ["items"]:
            id_to_category[category["id"]] = category["snippet"]["title"]
    combined_data["category"] = combined_data["category_id"].map(id_to_category)
    # print(combined_data.info())
    return combined_data
def clean_data(df):
    df['trending_date'] = pd.to_datetime(df["trending_date"],format ="%y.%d.%m")
    df['publish_time'] = pd.to_datetime(df["publish_time"],format = "%Y-%m-%dT%H:%M:%S.%fZ")
    return df

def main():
    df = load_data()

    df = clean_data(df)

    print(df.info())
if __name__== "__main__":
    main()