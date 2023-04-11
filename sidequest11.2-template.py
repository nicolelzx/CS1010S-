#
# CS1010S --- Programming Methodology
#
# Side Quest 11.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json

# Reading json file
def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google ;)

    For example, cs1010s-fbdata.json contains:
    {
        "members": {
            "data": [
                 {
                    "name": "Sunyoung Hwang",
                    "id": "970478132994592"
                 },
                 {
                    "name": "Nguy\u1ec5n Th\u1ea3o Ng\u00e2n",
                    "id": "790182697716021"
                 },
                 {
                    "name": "Tu Anh",
                    "id": "10201625605746698"
                 },
                 ...
             ]
        },
        ...
        "description": "This is the official FB Group for CS1010S: Programming Methodology taught in Python.",
        "name": "CS1010S",
        "feed": {
            "data": [
                 {
                    "message": "Yay! :D \n\nhttps://www.facebook.com/saosin1994/posts/10204422037065788",
                    "from": {
                       "name": "Jeffrey Lee",
                       "id": "718371011538995"
                    },
                    "name": "If you're new to coding, this is the programming language you should learn first",
                    "id": "422428264540999_888704734580014",
                    "likes": {
                       "data": [
                          {
                             "id": "187291868313225",
                             "name": "May Tan"
                          },
                          {
                             "id": "10153290038157072",
                             "name": "Goh See Ting"
                          }
                       ],
                       ...
                    }
                }
            ]
        }
    }
    """
    datafile = open(filename, 'r',  encoding='utf-8')
    return json.loads(datafile.read())

# CS1010S Facebook Group Data as a dictionary object
fb_data = read_json('cs1010s-fbdata.json')

##########
# Task a #
##########

def count_comments(data):
    lst = data["feed"]["data"] #list of dicts [comments][data] list of dicts
    count = 0
    for d in lst:
        if "comments" in d.keys():
            count += len(d["comments"]["data"])
        else:
            continue
    return count

#print("Number of Comments in CS1010S: ", count_comments(fb_data))

##########
# Task b #
##########

def count_likes(data):
    lst = data["feed"]["data"]
    count = 0
    for d in lst:
        if "likes" in d.keys():
            in_list = d["likes"]["data"]
            count += len(in_list)
        if "comments" in d.keys():
            in_list2 = d["comments"]["data"]
            for d in in_list2:
                count += d["like_count"]
        continue
    return count            

#print("Number of Likes in CS1010S: ", count_likes(fb_data))

##########
# Task c #
##########

def create_member_dict(data):
    lst = data["members"]["data"]
    result = {}
    for member in lst:
        key = member['id']
        value = {k:v for k,v in member.items() if k!="id"}
        result[key] = value
    return result
        
    # Lookup table where key is id and value is member data object
    #{id: member data object 

member_dict = create_member_dict(fb_data)
#print(member_dict["10202689170610256"])

# To ponder upon:
    # Q: Why did we choose the id of the member data object to be the key?
    # A: 

    # Q: It is inappropriate to use the name as the key. What will happen if we use the name as the key of member_dict?
    # A:

##########
# Task d #
##########

def posts_freq(data):
    # Returns a dict where key is fb_id and value is number of posts in feed
    result = {} # result[fb_id] = no. of posts
    lst = data["feed"]["data"]
    for i in lst:
        id_no = i["from"]["id"]
        if id_no not in result:
            result[id_no] = 1
        else:
            result[id_no] += 1
    return result

#print("Posts Frequency: ", posts_freq(fb_data))

##########
# Task e #
##########

def comments_freq(data):
    # result[fb_id] = no. of comments
    result = {}     
    lst = data["feed"]["data"]
    
    for i in lst:   # i is dict
        if "comments" in i:
            in_list = i["comments"]["data"]
            for j in in_list:   # j is dict
                id_no = j["from"]["id"]
                if id_no not in result:
                    result[id_no] = 1
                else:
                    result[id_no] += 1
        else:
            continue
    return result
    

#print("Comments Frequency: ", comments_freq(fb_data))

##########
# Task f #
##########

def likes_freq(data):
    # result[fb_id] = no. of likes in feed
    result = {}     
    lst = data["feed"]["data"]
    for i in lst:
        if "likes" not in i:
            continue
        else:
            in_list = i["likes"]["data"]
            for j in in_list:
                if j["id"] in result:
                    result[j["id"]] += 1
                else:
                    result[j["id"]] = 1
    return result
            

#print("Likes Frequency: ", likes_freq(fb_data))

##########
# Task g #
##########

def popularity_score(data):
    # result[fb_id] = no. of likes a person's posts and comments hv
    lst = data["feed"]["data"]
    result = {}
    for post in lst:
        if "likes" in post:
            id_no = post["from"]["id"]
            num_likes = len(post["likes"]["data"])
            if id_no not in result:
                result[id_no] = num_likes
            else:
                result[id_no] += num_likes
        else:
            continue
    for post in lst:
        if "comments" not in post:
            continue
        else:
            in_list = post["comments"]["data"]
            for j in in_list:
                id_no = j["from"]["id"]
                num = j["like_count"]
                if id_no not in result:
                    result[id_no] = num
                else:
                    result[id_no] += num
    result = {k:v for k,v in result.items() if v!=0}           
    return result

#print("Popularity Score: ", popularity_score(fb_data))

##########
# Task h #
##########

def member_stats(data):
    # Expand the member dict to include the keys:
    # 'posts_count', 'comments_count' and 'likes_count'
    posts = posts_freq(data)
    comments = comments_freq(data)
    likes = likes_freq(data)
    new_data = create_member_dict(data) # id: {name, gender}
    
    for id_no,m in new_data.items():
        if id_no in posts:
            p = posts[id_no]
            m["posts_count"] = p
        else:
            p = 0
            m["posts_count"] = p

    for id_no,m in new_data.items():
        if id_no in comments:
            c = comments[id_no]
            m["comments_count"] = c
        else:
            c = 0
            m["comments_count"] = c

    for id_no,m in new_data.items():
        if id_no in likes:
            l = likes[id_no]
            m["likes_count"] = l
        else:
            l = 0
            m["likes_count"] = l

    return new_data
        
stats = member_stats(fb_data)
#print(stats["625742960877771"], '\n')

##########
# Task i #
##########

def activity_score(data):
    data = member_stats(data)
    for id_no, m in data.items():
        value = m["posts_count"]*3 + m["comments_count"]*2 + m["likes_count"]
        data[id_no] = value
    return data

scores = activity_score(fb_data)
# print(scores["806647796032627"]) # => 25
# print(scores["773847432675142"]) # => 0


##########
# Task j #
##########

def active_members_of_type(data, k, type_fn):
    # This is a higher order function, where type is a function and
    # can be either posts_freq, comments_freq, likes_freq, etc
    # and filters out the pairs that have frequency >= k
    mem_d = create_member_dict(data)
    new_data = type_fn(data)
    new_data = list([k,v] for k,v in new_data.items())
    new_data = list(filter(lambda x: x[1]>=k, new_data))

    result = []
    for i in new_data:
        id_no = i[0]
        value = i[1]
        if id_no in mem_d:
            name = mem_d[id_no]["name"]
            result.append([name,value])
    result = sorted(result)
    result = sorted(result, key = lambda x: -x[1])
    return result
    

print(active_members_of_type(fb_data, 2, posts_freq))

print(active_members_of_type(fb_data, 20, comments_freq))

print(active_members_of_type(fb_data, 40, likes_freq))

print(active_members_of_type(fb_data, 20, popularity_score))

print(active_members_of_type(fb_data, 80, activity_score))


########### DO NOT REMOVE THE TEST BELOW ###########

def gradeit():
    print("\n*** Facebook Stalker Autograding ***")
    print('==================')
    answers = json.loads(open('grading.json', 'r',  encoding='utf-8').read())
    total, correct = 0, 0
    def pass_or_fail(code, answer):
        nonlocal total
        total += 1
        if code == answer:
            nonlocal correct
            correct += 1
            return 'Passed!'
        else:
            return 'Failed.'
            
    print('Testing count_comments... ', pass_or_fail(count_comments(fb_data), answers['count_comments']))
    print('Testing count_likes... ', pass_or_fail(count_likes(fb_data), answers['count_likes']))
    print('Testing create_member_dict... ', pass_or_fail(create_member_dict(fb_data), answers['create_member_dict']))
    print('Testing posts_freq... ', pass_or_fail(posts_freq(fb_data), answers['posts_freq']))
    print('Testing comments_freq... ', pass_or_fail(comments_freq(fb_data), answers['comments_freq']))
    print('Testing likes_freq... ', pass_or_fail(likes_freq(fb_data), answers['likes_freq']))
    print('Testing popularity_score... ', pass_or_fail(popularity_score(fb_data), answers['popularity_score']))
    print('Testing member_stats... ', pass_or_fail(member_stats(fb_data), answers['member_stats']))
    print('Testing activity_score... ', pass_or_fail(activity_score(fb_data), answers['activity_score']))
    print('Testing members with >= 1 posts... ', pass_or_fail(active_members_of_type(fb_data, 1, posts_freq), answers['active_posters']))
    print('Testing members with >= 4 comments... ', pass_or_fail(active_members_of_type(fb_data, 4, comments_freq), answers['active_commenters']))
    print('Testing members with >= 4 likes... ', pass_or_fail(active_members_of_type(fb_data, 4, likes_freq), answers['active_likers']))
    print('Testing members who have >= 3 likes... ', pass_or_fail(active_members_of_type(fb_data, 3, popularity_score), answers['popular']))
    print('Testing members with an activity score of >= 10... ', pass_or_fail(active_members_of_type(fb_data, 10, activity_score), answers['overall_active']))
    print('==================')
    print('Grades: ' + str(correct) + '/' + str(total) + '\n')

gradeit()
