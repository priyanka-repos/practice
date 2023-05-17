agg_store =[
    
    
    {
        '$group': {
            '_id': 0, 
            'totalprice': {
                '$sum': '$price'
            }
        }
    }, {
        '$project': {
            '_id': 0
        }
    }


]