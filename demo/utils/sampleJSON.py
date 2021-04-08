import uuid

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