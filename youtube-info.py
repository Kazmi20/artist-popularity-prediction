import requests

API_KEY = 'AIzaSyDKf7ZURIkyvJWoRP4dpq6DLmvOkYP3110'  
SEARCH_TERM = 'Blinding Lights'  


search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={SEARCH_TERM}&type=video&maxResults=1&key={API_KEY}"
search_response = requests.get(search_url)
search_data = search_response.json()

if 'items' in search_data and len(search_data['items']) > 0:
    video_id = search_data['items'][0]['id']['videoId']
    channel_id = search_data['items'][0]['snippet']['channelId']

    
    video_url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={API_KEY}"
    video_response = requests.get(video_url)
    video_data = video_response.json()
    
    if 'items' in video_data and len(video_data['items']) > 0:
        view_count = video_data['items'][0]['statistics'].get('viewCount', 'N/A')

        
        channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={API_KEY}"
        channel_response = requests.get(channel_url)
        channel_data = channel_response.json()

        if 'items' in channel_data and len(channel_data['items']) > 0:
            subscriber_count = channel_data['items'][0]['statistics'].get('subscriberCount', 'N/A')

            print(f"Video ID: {video_id}")
            print(f"View Count: {view_count}")
            print(f"Channel Subscriber Count: {subscriber_count}")
        else:
            print("Channel details not found.")
    else:
        print("Video details not found.")
else:
    print("No videos found for the search term.")
