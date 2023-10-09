from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import psycopg2
import pandas as pd
import numpy as np



# load database login info
df = pd.read_csv('credentials.csv')
credentials = np.array(df)[:]

DB_NAME = credentials[0][0]
DB_USER = credentials[0][1]
DB_PASS = credentials[0][2]
DB_HOST = credentials[0][3]
DB_PORT = credentials[0][4]


# load jinja2 templates
templates = Jinja2Templates(directory='templates')



# FastAPI app
app = FastAPI()


# Homepage
@app.get('/')
async def root(request: Request):
	return templates.TemplateResponse(
			'home.html'
			, {
				'request': request
				, 'greeting': 'Welcome to Promptly!'
				}
	)


# one character prompts
@app.get('/one')
async def scenario(request: Request):
	# type of prompt
	ptype = 'single character'
	
	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM one ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('one char prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return templates.TemplateResponse(
			'prompt.html'
			, {
				'request': request
				, 'prompt': prompt
				, 'ptype':ptype
				}
	)



# two character prompts
@app.get('/two')
async def two(request: Request):
	# type of prompt
	ptype = 'two character' ## change to 'two character??'

	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM two ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('two char prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return templates.TemplateResponse(
			'prompt.html'
			, {
				'request': request
				, 'prompt': prompt
				, 'ptype': ptype
				}
	)


# three character prompts
@app.get('/three')
async def three(request: Request):
	# type of prompt
	ptype = 'three character'

	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM three ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('three char prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return templates.TemplateResponse(
			'prompt.html'
			, {
				'request': request
				, 'prompt': prompt
				, 'ptype': ptype
				}
	)


# dialogue prompts
@app.get('/dialogue')
async def dialogue(request: Request):
	# type of prompt
	ptype = 'dialogue'
	
	# connect to database
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)

	# open cursor to perform database operations
	cur = conn.cursor()

	# grab random dialogue prompt
	cur.execute(
		'SELECT * FROM dialogue ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('Dialogue prompt: ' + prompt)

	# close communication with database
	cur.close()
	conn.close()

	return templates.TemplateResponse(
			'prompt.html'
			, {
				'request': request
				, 'prompt': prompt
				, 'ptype': ptype
				}
	)


# drawing prompts
@app.get('/drawing')
async def drawing(request: Request):
	# type of prompt
	ptype = 'drawing'
	
	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM drawing ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('drawing prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return templates.TemplateResponse(
			'prompt.html'
			, {
				'request': request
				, 'prompt': prompt
				, 'ptype': ptype
				}
	)


# nsfw prompts
@app.get('/nsfw')
async def nsfw(request: Request):
	# type of prompt
	ptype = 'nsfw'
	
	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM nsfw ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('nsfw prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return templates.TemplateResponse(
			'prompt.html'
			, {
				'request': request
				, 'prompt': prompt
				, 'ptype': ptype
				}
	)


# prose prompts
@app.get('/prose')
async def prose(request: Request):
	# type of prompt
	ptype = 'prose'
	
	# connect to db and open cursor
	conn = psycopg2.connect(database=DB_NAME
				, user=DB_USER
				, password=DB_PASS
				, host=DB_HOST
				, port=DB_PORT)
	cur = conn.cursor()

	# grab random prompt
	cur.execute(
		'SELECT * FROM prose ORDER BY RANDOM() LIMIT 1;'
		)
	prompt = cur.fetchone()
	prompt = prompt[1]
	print('prose prompt: ' + prompt)

	# close connections
	cur.close()
	conn.close()

	return templates.TemplateResponse(
			'prompt.html'
			, {
				'request': request
				, 'prompt': prompt
				, 'ptype': ptype
				}
	)




if __name__ == '__main__':
	run(app='dialgue:app', reload=True, host='192.168.1.18', port=8000)

