from landing.models import Profile


def get_profile(backend, user, response, details, *args, **kwargs):
    url = None
    small_url = None
    profile = Profile.objects.get_or_create(user=user)[0]
    if backend.name == 'facebook':
        print(response)
        url = 'http://graph.facebook.com/{0}/picture?type=large'.format(response['id'])
        small_url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        if not profile.gender:
            profile.gender = 'n'
    elif backend.name == "twitter":
        # print(response)
        if response['profile_image_url'] != '':
            if not response.get('default_profile_image'):
                url = response.get('profile_image_url_https')
                small_url = response.get('profile_image_url_https')
                if url:
                    url = url.replace('_normal.', '.')
                if not profile.gender:
                    profile.gender = 'n'
    elif backend.name == "google-oauth2":
        # print(response)
        print(response)
        if response['picture']:
            small_url = response['picture']
            url = small_url.replace("sz=50", "sz=160")
        if not profile.gender:
            if response.get('gender'):
                profile.gender = response.get('gender')[0]
            else:
                profile.gender = 'n'
    profile.avatar_small = small_url
    profile.avatar = url
    profile.save()