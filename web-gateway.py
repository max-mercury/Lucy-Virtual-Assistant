#pip install web.py
import os
import yaml
import web

from GreyMatter.SenseCells.tts import tts

render = web.template.render('templates/')

urls = (
	'/','index',
	)

profile = open('profile.yaml')
profile_data = yaml.safe_load('profile')
profile.close()

#functioning variables 
name = profile_data[0]

tts('Welcome' + name + 'system are now ready to run.How can i help you?')

class index:
	def GET(self):
		return render.index()

	def POST(self):
		x = web.input(myfile={})
		filedir = os.getcwd() + '/uploads' #change this to the dir you want to store the file in
		if 'myfile' in x: 	#check if the file-object is created
			filepath = x.myfie.filename.replace('\\','/')
			#replace windows style slashes with linux one
			filename = filepath.split('/')[-1]
			#splits the command and chooses the last part (the filename woth extension)
			fout = open(filedir +'/'+filename,'w')
			#creates the dir where the uploaded file should be stored
			fout.write(x.myfile.file.read())
			#writes the file to the newly uploaded file
			fout.close()
			#closes the file upload complete
		os.system('python main2.py'+filename)

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()		

