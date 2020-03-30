from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

# from rasa_core.actions.action import Action
# from rasa_core.events import SlotSet

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
#from send import SendGmail
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import operator

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
    
    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"63163217253a26f16084d1dfb85e0f02"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        city_id=d1["location_suggestions"][0]["city_id"]
        cuisines_dict={'american': 1, 'andhra': 2, 'asian': 3, 'arabian': 4, 'bakery': 5, 'afghani': 6,'biryani': 7, 'bengali': 10, 'chettinad': 18, 'burmese': 22, 'chinese': 25, 'raw meats': 27,'cafe': 30, 'continental': 35, 'european': 38, 'fast food': 40, 'french': 45, 'goan': 47,'gujarati': 48, 'hyderabadi': 49, 'north indian': 50, 'italian': 55, 'japanese': 60, 'kerala': 62,'konkan': 63, 'kashmiri': 65, 'lebanese': 66, 'korean': 67, 'malaysian': 69, 'mediterranean': 70,'malwani': 71, 'mangalorean': 72, 'mexican': 73, 'mongolian': 74, 'mughlai': 75, 'pizza': 82,'seafood': 83, 'south indian': 85, 'portuguese': 87, 'rajasthani': 88, 'spanish': 89, 'street food': 90,'tibetan': 93, 'thai': 95, 'vietnamese': 99, 'desserts': 100, 'maharashtrian': 102, 'indonesian': 114,'nepalese': 117, 'singaporean': 119, 'cantonese': 121, 'australian': 131, 'belgian': 132, 'british': 133,'german': 134, 'middle eastern': 137, 'pakistani': 139, 'iranian': 140, 'steak': 141, 'turkish': 142,'healthy food': 143, 'egyptian': 146, 'moroccan': 147, 'indian': 148, 'tex-mex': 150,'greek': 156,'lucknowi': 157, 'brazilian': 159, 'coffee and tea': 161, 'peruvian': 162, 'tea': 163, 'juices': 164,'assamese': 165, 'burger': 168, 'armenian': 175, 'sushi': 177, 'kebab': 178, 'grill': 181, 'patisserie': 183,'deli': 192, 'bbq': 193, 'brasserie': 195, 'pan asian': 209, 'swiss': 213, 'israeli': 218, 'bar food': 227,'north eastern': 231, 'ice cream': 233, 'bubble tea': 247, 'drinks only': 268, 'oriya': 269, 'beverages': 270,'finger food': 271, 'fusion': 274, 'oriental': 278, 'parsi': 290, 'awadhi': 292, 'modern european': 294,'fish and chips': 298, 'sandwich': 304, 'vegetarian': 308, 'satay': 312, 'asian fusion': 401, 'falafel': 571,'eastern european': 651, 'crepes': 881, 'modern australian': 969, 'chili': 971, 'south american': 972,'yum cha': 978, 'dumplings': 985, 'panini': 989, 'sindhi': 993, 'charcoal chicken': 994, 'salad': 998,'roast chicken': 1005, 'bihari': 1013, 'cuisine varies': 1014, 'mithai': 1015, 'modern indian': 1018,'hot pot': 1022, 'rolls': 1023, 'wraps': 1024, 'fried chicken': 1025, 'bohri': 1032, 'vegan': 1034,'cafe food': 1039, 'coffee': 1040, 'paan': 1048}
        
        list1 = [0, 20, 40, 60, 80]
        d = []
        for i in list1:
            results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), limit=i)
            d1 = json.loads(results)
            d.extend(d1['restaurants'])
        
        response = []
        if len(d) == 0:
            response = []
        else:
            for restaurant in d:
                if str(price) == 'lesser than 300':
                    if restaurant['restaurant']['average_cost_for_two'] <300:
                        response.append([restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'],restaurant['restaurant']['average_cost_for_two'],float(restaurant['restaurant']['user_rating']['aggregate_rating'])])
                    else:
                        response
                elif str(price) == 'between 300 to 700':
                    if 300 <= restaurant['restaurant']['average_cost_for_two'] <700:
                        response.append([restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'],restaurant['restaurant']['average_cost_for_two'],float(restaurant['restaurant']['user_rating']['aggregate_rating'])])
                    else:
                        response
                else:
                    if restaurant['restaurant']['average_cost_for_two'] >=700:
                        response.append([restaurant['restaurant']['name'],restaurant['restaurant']['location']['address'],restaurant['restaurant']['average_cost_for_two'],float(restaurant['restaurant']['user_rating']['aggregate_rating'])])
                    else:
                        response
        
        if len(response) == 0:
            dispatcher.utter_message("Sorry, we couldn't find any restaurant in given budget/location/cuisine.")
        else:
            response = sorted(response, key=operator.itemgetter(3), reverse=True)
            top5 = response[:5]
            response_display = 'Showing you top 5 results in your budget range :' +"\n" + "\n"
            j = 0
            for i in top5:
                j = j + 1
                response_display = response_display + str(j) + ". " + i[0] + ' in ' + i[1] + ' has been rated ' + str(i[3]) + "\n" + "\n"
            dispatcher.utter_message("-----"+str(response_display))
            
            response_email = "Hi," + "\n" + "\n" 'Here is the list of the restaurants you requested - ' + "\n"
            top10 = response[:10]
            k = 0
            for i in top10:
                k = k + 1
                response_email = response_email + str(k) + ". " + i[0] + ' in ' + i[1] + ' has been rated - ' + str(i[3]) + ' and has average price for two people - Rs.' + str(i[2]) +"\n" + "\n"
            response_email = response_email + "Thanks," + "\n" + "Restaurant Chatbot"
            return [SlotSet('search_results',response_display),SlotSet('email_results',response_email )]


class SendMail(Action):
    def name(self):
        return 'action_send_email'
    
    def run(self, dispatcher, tracker, domain):
        recipient = tracker.get_slot('email')
        results = tracker.get_slot('email_results')
        try:
            # Create a secure SSL context
            #context = ssl.create_default_context()
            # set up the SMTP server
            msg = MIMEMultipart()
            senderemail = input("Type your email id and press enter: ")
            password = input("Type your email password and press enter: ")
            msg['From'] = senderemail
            msg['To'] = recipient
            msg['Subject'] = "Your restaurant search results"
            body = results
            msg.attach(MIMEText(body, 'plain'))
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(senderemail,password)
            text = msg.as_string()
            s.sendmail(senderemail, recipient,text )
        except Exception as e:
            print(e)
        finally:
            s.quit()
        dispatcher.utter_message("Sent")
        return [SlotSet('email', recipient)]

class Check_location(Action):
    def name(self):
        return 'action_check_location'
    
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        city_dict =['Ahmedabad','Amdavad','Bengaluru','Bangalore','Chennai','Madras','New Delhi','Delhi','Delhi NCR','Dehli','Dilli','Hyderabad','Kolkata','Calcutta','Mumbai','Bombay','Bambai','Pune','Poona','Agra','Ajmer','Aligarh','Amravati','Amritsar','Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi','Bhopal','Bhubaneswar','Bikaner','Bilaspur','Bokaro Steel City','Bokaro','Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad','Bhilai','Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur', 'Gulbarga','Guntur','Gwalior','Gurgaon','Gurugram','Guwahati','Hamirpur','Hubli–Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar','Jamshedpur','Jhansi','Jodhpur','Kakinada','Kannur','Kanpur','Kochi','Cochin','Kolhapur','Kollam','Kozhikode','Kurnool','Ludhiana','Lucknow','Madurai','Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore','Mysuru','Nagpur','Nanded','Nashik', 'Nellore','Noida','Patna','Pondicherry','Purulia Prayagraj','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Shimla','Siliguri','Solapur','Srinagar','Surat','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tiruppur','Ujjain','Bijapur','Vadodara','Varanasi', 'Benares','Banaras','Vasai-Virar City','Vasai-Virar','Vasai Virar','Vijayawada','Visakhapatnam','Vellore,Warangal','Ahmedabad','Belagama','Hubballi','Calicut','Mangaluru','Trivandrum','Trichy']
        
        city_dict = [x.lower() for x in city_dict]
        
        if loc.lower() not in city_dict:
            location_f = 'tier3'
            dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location.")
            return [SlotSet('location_found', location_f)]
        else:
            location_f = 'found'
            return [SlotSet('location', loc), SlotSet('location_found', location_f)]