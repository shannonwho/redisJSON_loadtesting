import uuid

#Sample from Twitter
highlyNestedObj=[{
  "created_at": "Thu Jun 22 21:00:00 +0000 2017",
  "id": 877994604561387500,
  "id_str": "877994604561387520",
  "text": "Creating a Grocery List Manager Using Angular, Part 1: Add &amp; Display Items https://t.co/xFox78juL1 #Angular",
  "truncated": False,
  "entities": {
    "hashtags": [{
      "text": "Angular",
      "indices": [103, 111]
    }],
    "symbols": [],
    "user_mentions": [],
    "urls": [{
      "url": "https://t.co/xFox78juL1",
      "expanded_url": "http://buff.ly/2sr60pf",
      "display_url": "buff.ly/2sr60pf",
      "indices": [79, 102]
    }]
  },
  "source": "<a href=\"http://bufferapp.com\" rel=\"nofollow\">Buffer</a>",
  "user": {
    "id": 772682964,
    "id_str": "772682964",
    "name": "SitePoint JavaScript",
    "screen_name": "SitePointJS",
    "location": "Melbourne, Australia",
    "description": "Keep up with JavaScript tutorials, tips, tricks and articles at SitePoint.",
    "url": "http://t.co/cCH13gqeUK",
    "entities": {
      "url": {
        "urls": [{
          "url": "http://t.co/cCH13gqeUK",
          "expanded_url": "https://www.sitepoint.com/javascript",
          "display_url": "sitepoint.com/javascript",
          "indices": [0, 22]
        }]
      },
      "description": {
        "urls": []
      }
    },
    "protected": False,
    "followers_count": 2145,
    "friends_count": 18,
    "listed_count": 328,
    "created_at": "Wed Aug 22 02:06:33 +0000 2012",
    "favourites_count": 57,
    "utc_offset": 43200,
    "time_zone": "Wellington",
  },
    "scondaryUser": {
    "id": 772682964,
    "id_str": "772682964",
    "name": "SitePoint JavaScript",
    "screen_name": "SitePointJS",
    "location": "Melbourne, Australia",
    "description": "Keep up with JavaScript tutorials, tips, tricks and articles at SitePoint.",
    "url": "http://t.co/cCH13gqeUK",
    "entities": {
      "url": {
        "urls": [{
          "url": "http://t.co/cCH13gqeUK",
          "expanded_url": "https://www.sitepoint.com/javascript",
          "display_url": "sitepoint.com/javascript",
          "indices": [0, 22]
        }]
      },
      "description": {
        "urls": []
      }
    },
    "protected": False,
    "followers_count": 2145,
    "friends_count": 18,
    "listed_count": 328,
    "created_at": "Wed Aug 22 02:06:33 +0000 2012",
    "favourites_count": 57,
    "utc_offset": 43200,
    "time_zone": "Wellington",
  },
   "thirdUser": {
    "id": 772682964,
    "id_str": "772682964",
    "name": "SitePoint JavaScript",
    "screen_name": "SitePointJS",
    "location": "Melbourne, Australia",
    "description": "Keep up with JavaScript tutorials, tips, tricks and articles at SitePoint.",
    "url": "http://t.co/cCH13gqeUK",
    "entities": {
      "url": {
        "urls": [{
          "url": "http://t.co/cCH13gqeUK",
          "expanded_url": "https://www.sitepoint.com/javascript",
          "display_url": "sitepoint.com/javascript",
          "indices": [0, 22]
        }]
      },
      "description": {
        "urls": []
      }
    },
    "protected": False,
    "followers_count": 2145,
    "friends_count": 18,
    "listed_count": 328,
    "created_at": "Wed Aug 22 02:06:33 +0000 2012",
    "favourites_count": 57,
    "utc_offset": 43200,
    "time_zone": "Wellington",
  }
}]


"""
'array_of_docs' : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    },
    {
    	   "sclr" : 12,
        "str" : "g",
        "arr" : [7,8,9,{"sclr" : 22, "str" : "h"}]
        },
    -2
    ]
"""

smallObj= {
'id': "smallStaticObj:" + str(uuid.uuid4()),
'sclr' : 0,
'str' : "b",
'sub_doc' : {
	"sclr" : 10,
	"str" : "c",
	"arr" : [1,2,3,{"sclr" : 20, "str":"d"}]
},
'array_of_docs' : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }]
}


"""
"object with 1 member":["array with 1 element"]},
    {},
    [],
    -42,
    true,
    false,
    null,
"""
bigObj = {
    "id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string",
"id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string",
"id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string",
"id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string",
"id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string",
"id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string",
"id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string",
"id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string",
"id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string",
"id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string",
"id": "bigStaticObj:" + str(uuid.uuid4()),
    "integer": 1234567890,
    "real": -9876.543210,
    "e": 0.123456789e-12,
    "E": 1.234567890E+34,
    "":  23456789012E66,
    "zero": 0,
    "one": 1,
    "space": " ",
    "quote": "\"",
    "backslash": "\\",
    "controls": "\b\f\n\r\t",
    "slash": "/ & \/",
    "alpha": "abcdefghijklmnopqrstuvwyz",
    "ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWYZ",
    "digit": "0123456789",
    "0123456789": "digit",
    "special": "`1~!@#$%^&*()_+-={':[,]}|;.</>?",
    "hex": "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
    "true": True,
    "false": False,
    "null": "null",
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array_of_docs" : [
    -1,
    {	       
        "sclr" : 11,
        "str" : "e",
        "arr" : [4,5,6,{"sclr" : 21, "str" : "f"}]
    }],
    "array":[  ],
    "object":{  },
    "address": "50 St. James Street",
    "url": "http://www.JSON.org/",
    "comment": "// /* <!-- --",
    "# -- --> */": " ",
    " s p a c e d " :[1,2 , 3

,

4 , 5        ,          6           ,7        ],"compact":[1,2,3,4,5,6,7],
    "jsontext": "{\"object with 1 member\":[\"array with 1 element\"]}",
    "quotes": "&#34; \u0022 %22 0x22 034 &#x22;",
    "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|;:',./<>?"
: "A key can be any string"
    }