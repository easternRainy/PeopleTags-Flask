

persons = [{
			"id": f"person_id{i}",
			"first": f"first{i}", 
			"last":f"last{i}" , 
			"age":f"age{i}",
			"jobTitle": f"jobTitle{i}" ,
			"email":f"email{i}@server.com", 
			"description": f"description{i}"
			} 

			for i in range(10)
		]

groups = [{
			"id": f"group_id{i}",
			"name": f"group{i}", 
			"description": f"description{i}"
			} 

			for i in range(10)
		]


posts = [{
			"id": f"post_id{i}",
			"content": f"content{i}", 
			"visibility": f"visibility{i}",
			"createdTime": f"createdTime{i}"
			} 

			for i in range(10)
		]

socialMedias = [{
	"socialMediaName": f"socialMediaName{i}",
	"socialMediaLink": f"socialMediaLink{i}"
	}

	for i in range(10)
]