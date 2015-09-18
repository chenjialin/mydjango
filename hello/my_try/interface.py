#coding: utf-8
import urllib2
from xml.etree import ElementTree
from models import Music_info


def get_xml_data():
    url = "http://ax.phobos.apple.com.edgesuite.net/WebObjects/MZStore.woa/wpa/MRSS/newreleases/limit=300/rss.xml"
    req = urllib2.Request(url)
    con = urllib2.urlopen(req)
    doc = con.read()
    con.close()

    return doc


def parse_xml(xml_str):
    all_data = []
    root = ElementTree.fromstring(xml_str)
    all_item = root.getiterator("item")
    for item in all_item:
        data = {}
        children = item.getchildren()
        for i in children:
            if 'artistLink' in i.tag:
                data['artistLink'] = i.text
            elif 'artist' in i.tag:
                data['artist'] = i.text
            elif 'albumLink' in i.tag:
                data['albumLink'] = i.text
            elif 'albumPrice' in i.tag:
                data['albumPrice'] = i.text
            elif 'album' in i.tag:
                data['album'] = i.text
            elif 'category' in i.tag:
                data['category'] = i.text
            elif 'coverArt' in i.tag:
                data['coverArt'] = i.text
            elif 'releasedate' in i.tag:
                data['releasedate'] = i.text

        all_data.append(data)
    return all_data


def save_to_db(data):
    Music_info.objects.all().delete()
    for row in data:
        music_info = Music_info(artist=row.get('artist', '') or '',
                                artistLink=row.get('artistLink', '') or '',
                                album=row.get('album', '') or '',
                                albumLink=row.get('albumLink', '') or '',
                                albumPrice=row.get('albumPrice', '') or '',
                                category=row.get('category', '') or '',
                                coverArt=row.get('coverArt', '') or '',
                                releasedate=row.get('releasedate', '') or ''
                                )
        music_info.save()


def get_data_from_db():
    json_data = []
    data = Music_info.objects.all()
    for row in data:
        json_data.append({
            'artist': row.artist,
            'artistLink': row.artistLink,
            'album': row.album,
            'albumLink': row.albumLink,
            'albumPrice': row.albumPrice,
            'category': row.category,
            'coverArt': row.coverArt,
            'releasedate': row.releasedate
        })

    return json_data