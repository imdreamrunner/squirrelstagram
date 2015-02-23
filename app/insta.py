import urlparse
from instagram.client import InstagramAPI
from . import config
from .models import Media

__author__ = "imdreamrunner"
__email__ = "imdreamrunner@gmail.com"


def get_media_list_by_tag(tag_name, count=None, max_tag_id=None):
    if count is None:
        count = 16
    api = InstagramAPI(client_id=config.AUTH["client_id"])
    if max_tag_id is None:
        original_media_list, next_url = api.tag_recent_media(tag_name=tag_name, count=count)
    else:
        original_media_list, next_url = api.tag_recent_media(tag_name=tag_name, count=count, max_tag_id=max_tag_id)
    # process media list
    media_list = list()
    for original_media in original_media_list:
        tag_list = []
        for tag in original_media.tags:
            tag_list.append(tag.name)
        image_dict = dict()
        for key, url in original_media.images.iteritems():
            image_dict[key] = str(url)
        video_dict = None
        if hasattr(original_media, "videos"):
            video_dict = dict()
            for key, url in original_media.videos.iteritems():
                video_dict[key] = str(url)
        media = Media(id=original_media.id,
                      type=original_media.type,
                      caption=original_media.caption.text,
                      user=original_media.user.username,
                      created_time=original_media.created_time,
                      tags=tag_list,
                      images=image_dict,
                      videos=video_dict)
        media_list.append(media)
    # get next_tag_id
    max_tag_id = None
    if next_url is not None:
        next_url_parsed = urlparse.urlparse(next_url)
        assert "max_tag_id" in urlparse.parse_qs(next_url_parsed.query)
        assert isinstance(urlparse.parse_qs(next_url_parsed.query)["max_tag_id"], list)
        assert len(urlparse.parse_qs(next_url_parsed.query)["max_tag_id"]) == 1
        max_tag_id = urlparse.parse_qs(next_url_parsed.query)["max_tag_id"][0]
    return media_list, max_tag_id

