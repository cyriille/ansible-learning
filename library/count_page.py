#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule  
import MySQLdb

def main():
    module = AnsibleModule(
        argument_spec=dict(
  	    db_name	= dict(required=True, type='str'),
  	    request	= dict(required=True, type='str'),
	    )
    )
    
    db_name_local = module.params.get('db_name')
    request_local = module.params.get('request')
 
    db = MySQLdb.connect(db=db_name_local)
    cur = db.cursor()
    cur.execute(request_local)
    results = cur.fetchall()
    db.close()
 
    module.exit_json(changed=False, resultat=results)  
 
if __name__ == "__main__":
    main()


DOCUMENTATION='''
module: count_page
author: Alexandre
description: Module qui permet d'executer une requete SQL
 
options:
  db_name:
	description: nom de la base de donnees
	required: yes
  request:
	description: requete a executer
	required: yes
 
'''

EXAMPLES='''
- name: "SQL"
  count_page:
	db_name: "BDD"
	request: "select * from user;"
'''


RETURN = '''
resultat:
	description: retourne le resultat de la requete
'''
