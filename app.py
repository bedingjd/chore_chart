from flask import Flask, render_template, request
import yaml
from datetime import datetime, date
import chore

app = Flask(__name__)

# global variable to hold all people info
allPeople = None

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)
        
def load_chores():
    with open('chores.yaml', 'r') as chore_file:
        return yaml.safe_load(chore_file)

def load_people():
    with open('people.yaml', 'r') as people_file:
        return yaml.safe_load(people_file)


def calculate_days_remaining(target_date):
    today = date.today()
    current_year = today.year

    target = datetime.strptime(f"{target_date}/{current_year}", "%m/%d/%Y").date()

    # If the date has already passed this year, use next year
    if target < today:
        target = target.replace(year=current_year + 1)

    difference = target - today
    return difference.days


def get_sorted_countdowns(countdowns):
    return sorted(
        countdowns,
        key=lambda x: calculate_days_remaining(x['date'])
    )


def get_recurring(people):
    people_count = len(people)
    days_into_year = datetime.now().timetuple().tm_yday
    todays_index = days_into_year % people_count
    return people[todays_index]

def convertDictToYaml(dict):
    converted = 'people:\n'
    p0 = dict['people']
    for p in p0:
        converted += "  - name: \"" + str(p['name']) + "\"\n"
        converted += '    id: ' + str(p['id']) + '\n'
        converted += '    bank_account: ' + str(p['bank_account']) + '\n'
        converted += "    image: \"" + str(p['image']) + "\"\n"
    # print(f"===> dictToYaml: {converted} \n")
    return converted


def update_People_Info(people):
    c = yaml.safe_load(people)
    with open('people.yaml', 'w') as file:
        yaml.dump(c, file)
    return


def update_chore_status(form, chores, people):
    thisID = list(form.keys())[0]
    print(f"===> ID : {thisID}\n")
    c0 = chores['chores']
    p0 = people['people']
    for chore in c0:
        print(f"==> checking chore: {chore['id']}\n")
        if int(chore['id']) == int(thisID):
            print(f'==> matched id: {thisID}\n')
            chore['status'] = 'DONE'
            personName = chore['person']
            value = chore['value']
            for p in p0:
                if p['name'] == personName:
                    p['bank_account'] += value

            
    return
    
def update_chore_status2(chore_id, chores, people):
    c0 = chores['chores']
    p0 = people['people']
    for chore in c0:
        print(f"==> checking chore: {chore['id']}\n")
        if int(chore['id']) == chore_id:
            print(f'==> matched id: {chore_id}\n')
            chore['status'] = 'DONE'
            personName = chore['person']
            value = chore['value']
            for p in p0:
                if p['name'] == personName:
                    p['bank_account'] += value

            
    return
            
    


@app.route('/', methods=['GET', 'POST'])
def index():
    config = load_config()
    allChores = load_chores()
    global allPeople
    allPeople = load_people()
    today = datetime.now().strftime("%A, %B %d")
    todayTime = datetime.now().strftime("%H:%M")

    for item in config['recurring']:
        item['today'] = get_recurring(item['people'])
        sorted_countdowns = get_sorted_countdowns(config['countdowns'])
        for countdown in sorted_countdowns:
            countdown['days_remaining'] = calculate_days_remaining(countdown['date'])


    if(request.method == 'POST'):
        form = request.form
        print(f"==> Button pressed, form info: {form}\n")
        #print(f"==> ID {form['1']}")
        
        update_chore_status(form, allChores, allPeople)
        '''
        print(f"...allPeople is {allPeople}")
        p0 = allPeople['people']
        for p in p0:
            print(f"people is {p}")
            if p['name'] == 'Jamie':
                p['bank_account'] += 1.00
        #print(f"===> Converted \n{convertDictToYaml(allPeople)} \n")
        '''
        update_People_Info(convertDictToYaml(allPeople))
        #update_chore_status(form, allChores)
        return render_template('index.html',
				   today=today,
				   todayTime = todayTime,
				   recurring=config['recurring'],
				   countdowns=sorted_countdowns,
				   chores = allChores['chores'],
                                   peeps = allPeople['people'])
    else:
        # config = load_config()
        # allChores = load_chores()

            return render_template('index.html',
				   today=today,
				   todayTime = todayTime,
				   recurring=config['recurring'],
				   countdowns=sorted_countdowns,
				   chores = allChores['chores'],
                                   peeps = allPeople['people'])
                                   
@app.route('/update_chore/<int:chore_id>', methods=['GET', 'POST'])
def update_chore(chore_id):
    config = load_config()
    allChores = load_chores()
    global allPeople
    allPeople = load_people()
    today = datetime.now().strftime("%A, %B %d")
    todayTime = datetime.now().strftime("%H:%M")
    
    for item in config['recurring']:
        item['today'] = get_recurring(item['people'])
        sorted_countdowns = get_sorted_countdowns(config['countdowns'])
        for countdown in sorted_countdowns:
            countdown['days_remaining'] = calculate_days_remaining(countdown['date'])
    
    update_chore_status2(chore_id, allChores, allPeople)
    update_People_Info(convertDictToYaml(allPeople))
    
    if(request.method == 'POST'):
        form = request.form
        print(f"==> Button pressed, form info: {form}\n")
        
        update_chore_status(form, allChores, allPeople)

        update_People_Info(convertDictToYaml(allPeople))
    
    return render_template('index.html',
				   today=today,
				   todayTime = todayTime,
				   recurring=config['recurring'],
				   countdowns=sorted_countdowns,
				   chores = allChores['chores'],
                            peeps = allPeople['people'])
    
    


if __name__ == '__main__':
    app.run(debug=True)
