tweetTraining = [
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': "1"
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': "0"
            }
        ]
    },

    {
        'sentence': "the cake is bad but not the tea",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "cake",
                'sentiment': "bad",
                'polarity': "0"
            },
            {
                'entity': "starbucks",
                'aspect': "tea",
                'sentiment': "great",
                'polarity': "1"
            }
        ]
    },
    {
        'sentence': "i dont like frappucino but i like machiato",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "machiato",
                'sentiment': "like",
                'polarity': "1"
            },
            {
                'entity': "starbucks",
                'aspect': "frappucino",
                'sentiment': "do not like",
                'polarity': "0"
            }
        ]
    },
    {
        'sentence': "the coffe is not sweet but starbucks but i like the cake because its delicious",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994945",
        'aspects': [

            {
                'entity': "coffee",
                'aspect': "taste",
                'sentiment': "not sweet",
                'polarity': "0"
            },
            {
                'entity': "starbucks",
                'aspect': "cake",
                'sentiment': "delicious",
                'polarity': "1"
            }
        ]
    },
    {
        'sentence': "i like cafe starbucks because clean and the staff is beautiful but toilet dirty",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994945",
        'aspects': [

            {
                'entity': "starbucks",
                'aspect': "place",
                'sentiment': "clean",
                'polarity': "1"
            },
            {
                'entity': "starbucks",
                'aspect': "toilet",
                'sentiment': "dirty",
                'polarity': "0"
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "beautiful",
                'polarity': "1"
            }
        ]
    },
    {
        'sentence': "the taste the coffee is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994945",
        'aspects': [

            {
                'entity': "coffee",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': "0"
            }
        ]
    }
]

tesTweetsAspectBase = [
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    }


]

tesTweetsAspectBase1 = [
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994947",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but starbucks staff is ugly",
        'created_at': "2017-03-08",
        'user_id': "2244994945",
        'tweet_id': "2244994941",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "staff",
                'sentiment': "ugly",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "I love starbucks but not the milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994946",
        'tweet_id': "2244994942",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "general",
                'sentiment': "love",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not love",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like starbucks in chicago because the table is dirty and small but cashier is beutiful",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994943",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "table",
                'sentiment': "dirty and small",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "cashier",
                'sentiment': "beautiful",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "i dont like frappuchino and milk tea",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994944",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste frappuchino and milk tea is bad",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994945",
        'aspects': [
            {
                'entity': "starbucks",
                'aspect': "frappuchino",
                'sentiment': "not like",
                'polarity': ""
            },
            {
                'entity': "starbucks",
                'aspect': "milk tea",
                'sentiment': "not like",
                'polarity': ""
            }
        ]
    },
    {
        'sentence': "the taste the milk tea not bad and the table is clean",
        'created_at': "2017-03-08",
        'user_id': "2244994947",
        'tweet_id': "2244994946",
        'aspects': [
            {
                'entity': "milk tea",
                'aspect': "taste",
                'sentiment': "not bad",
                'polarity': ""
            },
            {
                'entity': "milk tea",
                'aspect': "table",
                'sentiment': "clean",
                'polarity': ""
            }
        ]
    }
]

# tweet = {
#     'sentence': "I love starbucks but starbucks staff is ugly",
#     'created_at': "2017-03-08",
#     'user_id': "2244994945",
#     'aspects': [
#         {
#             'entity': "starbucks",
#             'aspect': "general",
#             'sentiment': "love",
#             'polarity': "positive"
#         },
#         {
#             'entity': "starbucks",
#             'aspect': "staff",
#             'sentiment': "ugly",
#             'polarity': "negative"
#         },
#         {
#             'entity': "starbucks",
#             'aspect': "staff",
#             'sentiment': "do not like",
#             'polarity': "negative"
#         },
#         {
#             'entity': "starbucks",
#             'aspect': "staff",
#             'sentiment': "do not love",
#             'polarity': "negative"
#         }
#     ]
# }
#
# aspect_tweets = [
#     {
#         'sentence': "I love starbucks but starbucks staff is ugly",
#         'created_at': "2017-03-08",
#         'user_id': "2244994945",
#         'aspects': [
#             {
#                 'entity': "starbucks",
#                 'aspect': "general",
#                 'sentiment': "love",
#                 'polarity': "positive"
#             },
#             {
#                 'entity': "starbucks",
#                 'aspect': "staff",
#                 'sentiment': "ugly",
#                 'polarity': "negative"
#             },
#             {
#                 'entity': "starbucks",
#                 'aspect': "coffee",
#                 'sentiment': "not sweet",
#                 'polarity': "negative"
#             },
#             {
#                 'entity': "starbucks",
#                 'aspect': "cake",
#                 'sentiment': "delicious",
#                 'polarity': "positive"
#             }
#         ]
#     },
#     {
#         'sentence': "I love starbucks but starbucks staff is ugly",
#         'created_at': "2017-03-08",
#         'user_id': "2244994945",
#         'aspects': [
#             {
#                 'entity': "starbucks",
#                 'aspect': "general",
#                 'sentiment': "not love",
#                 'polarity': "negative"
#             },
#             {
#                 'entity': "starbucks",
#                 'aspect': "staff",
#                 'sentiment': "beautiful",
#                 'polarity': "positive"
#             },
#             {
#                 'entity': "starbucks",
#                 'aspect': "staff",
#                 'sentiment': "do not like",
#                 'polarity': "negative"
#             },
#             {
#                 'entity': "starbucks",
#                 'aspect': "staff",
#                 'sentiment': "do not love",
#                 'polarity': "negative"
#             }
#         ]
#     }
# ]

# pos_tweets = [('very sweet', 'positive'),
#               ('very beautiful', 'positive'),
#               ('a', 'positive'),
#               ('like', 'positive'),
#               ('love', 'positive'),
#               ('great', 'positive'),
#               ('the coffee is warm', 'positive')]
#
# neg_tweets = [('ugly', 'negative'),
#               ('not like','negative'),
#               ('not love', 'negative'),
#               ('not', 'negative'),
#               ('cup small', 'negative'),
#               ('dirty', 'negative'),
#               ('the weather is warm', 'negative')]



# all_tweets = [('very sweet', 'positive'),
#               ('very beautiful', 'positive'),
#               ('a', 'positive'),
#               ('like', 'positive'),
#               ('love', 'positive'),
#               ('great', 'positive'),
#               ('the coffee is warm', 'positive'),
#               ('ugly', 'negative'),
#               ('not like','negative'),
#               ('not love', 'negative'),
#               ('not', 'negative'),
#               ('cup small', 'negative'),
#               ('dirty', 'negative'),
#               ('the weather is warm', 'negative')]