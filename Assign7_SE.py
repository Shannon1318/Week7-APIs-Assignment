import requests

def extractData():
    CLIENT_ID = 'your client ID here'
    CLIENT_SECRET = 'your Secret here'

    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,})

    # convert the response to JSON
    auth_response_data = auth_response.json()
    # save the access token
    access_token = auth_response_data['access_token']

    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
        }
    # base URL for Spotify API
    BASE_URL = 'https://api.spotify.com/v1/'

    #ID for the artist OneRepublic
    artist_id = '5Pwc4xIPtQLFEnJriah9YJ'

    #Request the top 10 tracks for OneRepublic in the USA
    h = requests.get(BASE_URL + 'artists/' + artist_id + '/top-tracks/',
                 headers=headers, params={'country': 'US'})
    i = h.json()
    return i

def intoDict(i):
    #initialize list and dictionary
    data = []
    j = {}
    #Store title, popularity rating, album name, and release date in dictionary j, add to list
    for track in i['tracks']:
        j = {'track name': track['name'], 'popularity rating': track['popularity'],
            'album name': track['album']['name'],
            'release date': track['album']['release_date']}
        data.append(j)
    return data

def intoText(data):
    #Create text file and write to it
    filename = "text file.txt"
    outfile = open(filename, 'w')

    #Column Headers
    outfile.write("Track Name:\tPopularity Level:\tAlbum Name:\tRelease Date:")
    #Loop through and do a line for each track with the corresponding info
    for track in data:
        outfile.write("\n")
        outfile.write(str(track['track name'])+"\t"+"\t"+str(track['popularity rating'])+"\t"+"\t"
                      + str(track['album name'])+"\t"+"\t"+str(track['release date']))

def main():
    #function to extract data
    i = extractData()
    #store in dictionary (well, list of dictionaries)
    data = intoDict(i)
    #function to put the data into a text file
    intoText(data)

main()