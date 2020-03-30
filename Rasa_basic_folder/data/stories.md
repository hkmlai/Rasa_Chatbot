
## complete path2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_found": "found"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Pishu's (rated 4.3) in Shop .9, nandkripa shopping centre, ratan nagar, GANESH SAI MANDIR,  near Pp mithaiwala, opp Punjab dairy farm, bungalows,  andheri west and the average price for two people is Rs.400\nBruciato Food Factory (rated 4.3) in Shop 17, Rainbow Tower, Sector 20, Airoli, Navi Mumbai and the average price for two people is Rs.500\n99 Pizzeria (rated 4.3) in Shop 3, Ground Floor, Sai Krishna Kunj, Ganesh Chowk, DN Nagar, Versova, Andheri West, Mumbai and the average price for two people is Rs.550\nBohemia the Lounge (rated 4.3) in Shop 1-3, First Floor, XL Plaza, IIT PACE Junior College, IIT Market, Powai, Mumbai and the average price for two people is Rs.600\nWoodz Pizza (rated 4.3) in Shop 745, Adarsh Nagar, New Link Road, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.500\nPishu's (rated 4.1) in 8, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.400\nLa Crosta (rated 4.1) in Shop 8, Vakratund Society, Next To Yerela Medical College, Sector 4, Kharghar, Navi Mumbai and the average price for two people is Rs.500\nBlack Olive (rated 4.1) in 1087, Adarsh Nagar, New Link Road, Behind Lotus Petrol Pump, Jogeswari West, Oshiwara, Andheri West, Mumbai and the average price for two people is Rs.600\nCheezzo By Pi (rated 4.0) in Shop 13/14, Sector 4, Near ITM College, Kharghar, Navi Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in 29, Linkway Estate, Link Road, Near North Exhange, Malad West, Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in Shop 2, Om Vithoba Rukmani Apartments, Juhu Road, Near ISCON Temple, Juhu, Mumbai and the average price for two people is Rs.400\nFuel Up (rated 3.9) in 7, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.450\nSquares Pizza And Cafe (rated 3.7) in Unit K 17, Sonal Heavy Industrial Estate, Ramchandra Lane Extension, Link Road, Malad West, Mumbai and the average price for two people is Rs.550\nJoe's Pizza (rated 3.6) in Shop 7, Plot 431, Katra Bhavan, 15th Road, Bandra, Khar West, Mumbai and the average price for two people is Rs.500\n"}
    - slot{"email_results": "Pishu's (rated 4.3) in Shop .9, nandkripa shopping centre, ratan nagar, GANESH SAI MANDIR,  near Pp mithaiwala, opp Punjab dairy farm, bungalows,  andheri west and the average price for two people is Rs.400\nBruciato Food Factory (rated 4.3) in Shop 17, Rainbow Tower, Sector 20, Airoli, Navi Mumbai and the average price for two people is Rs.500\n99 Pizzeria (rated 4.3) in Shop 3, Ground Floor, Sai Krishna Kunj, Ganesh Chowk, DN Nagar, Versova, Andheri West, Mumbai and the average price for two people is Rs.550\nBohemia the Lounge (rated 4.3) in Shop 1-3, First Floor, XL Plaza, IIT PACE Junior College, IIT Market, Powai, Mumbai and the average price for two people is Rs.600\nWoodz Pizza (rated 4.3) in Shop 745, Adarsh Nagar, New Link Road, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.500\nPishu's (rated 4.1) in 8, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.400\nLa Crosta (rated 4.1) in Shop 8, Vakratund Society, Next To Yerela Medical College, Sector 4, Kharghar, Navi Mumbai and the average price for two people is Rs.500\nBlack Olive (rated 4.1) in 1087, Adarsh Nagar, New Link Road, Behind Lotus Petrol Pump, Jogeswari West, Oshiwara, Andheri West, Mumbai and the average price for two people is Rs.600\nCheezzo By Pi (rated 4.0) in Shop 13/14, Sector 4, Near ITM College, Kharghar, Navi Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in 29, Linkway Estate, Link Road, Near North Exhange, Malad West, Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in Shop 2, Om Vithoba Rukmani Apartments, Juhu Road, Near ISCON Temple, Juhu, Mumbai and the average price for two people is Rs.400\nFuel Up (rated 3.9) in 7, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.450\nSquares Pizza And Cafe (rated 3.7) in Unit K 17, Sonal Heavy Industrial Estate, Ramchandra Lane Extension, Link Road, Malad West, Mumbai and the average price for two people is Rs.550\nJoe's Pizza (rated 3.6) in Shop 7, Plot 431, Katra Bhavan, 15th Road, Bandra, Khar West, Mumbai and the average price for two people is Rs.500\n"}
    - utter_ask_email
* send_email{"email": "asffdggfg@yahoo.com"}
    - slot{"email": "asffdggfg@yahoo.com"}
    - action_send_email
* goodbye
    - utter_goodbye


## complete path3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price": "lesser than 300"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "lesser than 300"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"search_results": "Pishu's (rated 4.3) in Shop .9, nandkripa shopping centre, ratan nagar, GANESH SAI MANDIR,  near Pp mithaiwala, opp Punjab dairy farm, bungalows,  andheri west and the average price for two people is Rs.400\nBruciato Food Factory (rated 4.3) in Shop 17, Rainbow Tower, Sector 20, Airoli, Navi Mumbai and the average price for two people is Rs.500\n99 Pizzeria (rated 4.3) in Shop 3, Ground Floor, Sai Krishna Kunj, Ganesh Chowk, DN Nagar, Versova, Andheri West, Mumbai and the average price for two people is Rs.550\nBohemia the Lounge (rated 4.3) in Shop 1-3, First Floor, XL Plaza, IIT PACE Junior College, IIT Market, Powai, Mumbai and the average price for two people is Rs.600\nWoodz Pizza (rated 4.3) in Shop 745, Adarsh Nagar, New Link Road, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.500\nPishu's (rated 4.1) in 8, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.400\nLa Crosta (rated 4.1) in Shop 8, Vakratund Society, Next To Yerela Medical College, Sector 4, Kharghar, Navi Mumbai and the average price for two people is Rs.500\nBlack Olive (rated 4.1) in 1087, Adarsh Nagar, New Link Road, Behind Lotus Petrol Pump, Jogeswari West, Oshiwara, Andheri West, Mumbai and the average price for two people is Rs.600\nCheezzo By Pi (rated 4.0) in Shop 13/14, Sector 4, Near ITM College, Kharghar, Navi Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in 29, Linkway Estate, Link Road, Near North Exhange, Malad West, Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in Shop 2, Om Vithoba Rukmani Apartments, Juhu Road, Near ISCON Temple, Juhu, Mumbai and the average price for two people is Rs.400\nFuel Up (rated 3.9) in 7, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.450\nSquares Pizza And Cafe (rated 3.7) in Unit K 17, Sonal Heavy Industrial Estate, Ramchandra Lane Extension, Link Road, Malad West, Mumbai and the average price for two people is Rs.550\nJoe's Pizza (rated 3.6) in Shop 7, Plot 431, Katra Bhavan, 15th Road, Bandra, Khar West, Mumbai and the average price for two people is Rs.500\n"}
     - slot{"email_results": "Pishu's (rated 4.3) in Shop .9, nandkripa shopping centre, ratan nagar, GANESH SAI MANDIR,  near Pp mithaiwala, opp Punjab dairy farm, bungalows,  andheri west and the average price for two people is Rs.400\nBruciato Food Factory (rated 4.3) in Shop 17, Rainbow Tower, Sector 20, Airoli, Navi Mumbai and the average price for two people is Rs.500\n99 Pizzeria (rated 4.3) in Shop 3, Ground Floor, Sai Krishna Kunj, Ganesh Chowk, DN Nagar, Versova, Andheri West, Mumbai and the average price for two people is Rs.550\nBohemia the Lounge (rated 4.3) in Shop 1-3, First Floor, XL Plaza, IIT PACE Junior College, IIT Market, Powai, Mumbai and the average price for two people is Rs.600\nWoodz Pizza (rated 4.3) in Shop 745, Adarsh Nagar, New Link Road, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.500\nPishu's (rated 4.1) in 8, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.400\nLa Crosta (rated 4.1) in Shop 8, Vakratund Society, Next To Yerela Medical College, Sector 4, Kharghar, Navi Mumbai and the average price for two people is Rs.500\nBlack Olive (rated 4.1) in 1087, Adarsh Nagar, New Link Road, Behind Lotus Petrol Pump, Jogeswari West, Oshiwara, Andheri West, Mumbai and the average price for two people is Rs.600\nCheezzo By Pi (rated 4.0) in Shop 13/14, Sector 4, Near ITM College, Kharghar, Navi Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in 29, Linkway Estate, Link Road, Near North Exhange, Malad West, Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in Shop 2, Om Vithoba Rukmani Apartments, Juhu Road, Near ISCON Temple, Juhu, Mumbai and the average price for two people is Rs.400\nFuel Up (rated 3.9) in 7, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.450\nSquares Pizza And Cafe (rated 3.7) in Unit K 17, Sonal Heavy Industrial Estate, Ramchandra Lane Extension, Link Road, Malad West, Mumbai and the average price for two people is Rs.550\nJoe's Pizza (rated 3.6) in Shop 7, Plot 431, Katra Bhavan, 15th Road, Bandra, Khar West, Mumbai and the average price for two people is Rs.500\n"}
   - utter_ask_email
* send_email{"email": "asffdggfg@rediffmail.com"}
    - slot{"email": "asffdggfg@rediffmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
    

 

## complete path5
* greet
    - utter_greet
* restaurant_search{"location": "delhi", "price": "lesser than 300", "cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": "lesser than 300"}
    - slot{"cuisine": "chinese"}
    - action_check_location
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"search_results": "Pishu's (rated 4.3) in Shop .9, nandkripa shopping centre, ratan nagar, GANESH SAI MANDIR,  near Pp mithaiwala, opp Punjab dairy farm, bungalows,  andheri west and the average price for two people is Rs.400\nBruciato Food Factory (rated 4.3) in Shop 17, Rainbow Tower, Sector 20, Airoli, Navi Mumbai and the average price for two people is Rs.500\n99 Pizzeria (rated 4.3) in Shop 3, Ground Floor, Sai Krishna Kunj, Ganesh Chowk, DN Nagar, Versova, Andheri West, Mumbai and the average price for two people is Rs.550\nBohemia the Lounge (rated 4.3) in Shop 1-3, First Floor, XL Plaza, IIT PACE Junior College, IIT Market, Powai, Mumbai and the average price for two people is Rs.600\nWoodz Pizza (rated 4.3) in Shop 745, Adarsh Nagar, New Link Road, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.500\nPishu's (rated 4.1) in 8, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.400\nLa Crosta (rated 4.1) in Shop 8, Vakratund Society, Next To Yerela Medical College, Sector 4, Kharghar, Navi Mumbai and the average price for two people is Rs.500\nBlack Olive (rated 4.1) in 1087, Adarsh Nagar, New Link Road, Behind Lotus Petrol Pump, Jogeswari West, Oshiwara, Andheri West, Mumbai and the average price for two people is Rs.600\nCheezzo By Pi (rated 4.0) in Shop 13/14, Sector 4, Near ITM College, Kharghar, Navi Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in 29, Linkway Estate, Link Road, Near North Exhange, Malad West, Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in Shop 2, Om Vithoba Rukmani Apartments, Juhu Road, Near ISCON Temple, Juhu, Mumbai and the average price for two people is Rs.400\nFuel Up (rated 3.9) in 7, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.450\nSquares Pizza And Cafe (rated 3.7) in Unit K 17, Sonal Heavy Industrial Estate, Ramchandra Lane Extension, Link Road, Malad West, Mumbai and the average price for two people is Rs.550\nJoe's Pizza (rated 3.6) in Shop 7, Plot 431, Katra Bhavan, 15th Road, Bandra, Khar West, Mumbai and the average price for two people is Rs.500\n"}
    - slot{"email_results": "Pishu's (rated 4.3) in Shop .9, nandkripa shopping centre, ratan nagar, GANESH SAI MANDIR,  near Pp mithaiwala, opp Punjab dairy farm, bungalows,  andheri west and the average price for two people is Rs.400\nBruciato Food Factory (rated 4.3) in Shop 17, Rainbow Tower, Sector 20, Airoli, Navi Mumbai and the average price for two people is Rs.500\n99 Pizzeria (rated 4.3) in Shop 3, Ground Floor, Sai Krishna Kunj, Ganesh Chowk, DN Nagar, Versova, Andheri West, Mumbai and the average price for two people is Rs.550\nBohemia the Lounge (rated 4.3) in Shop 1-3, First Floor, XL Plaza, IIT PACE Junior College, IIT Market, Powai, Mumbai and the average price for two people is Rs.600\nWoodz Pizza (rated 4.3) in Shop 745, Adarsh Nagar, New Link Road, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.500\nPishu's (rated 4.1) in 8, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.400\nLa Crosta (rated 4.1) in Shop 8, Vakratund Society, Next To Yerela Medical College, Sector 4, Kharghar, Navi Mumbai and the average price for two people is Rs.500\nBlack Olive (rated 4.1) in 1087, Adarsh Nagar, New Link Road, Behind Lotus Petrol Pump, Jogeswari West, Oshiwara, Andheri West, Mumbai and the average price for two people is Rs.600\nCheezzo By Pi (rated 4.0) in Shop 13/14, Sector 4, Near ITM College, Kharghar, Navi Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in 29, Linkway Estate, Link Road, Near North Exhange, Malad West, Mumbai and the average price for two people is Rs.400\nPishu's (rated 3.9) in Shop 2, Om Vithoba Rukmani Apartments, Juhu Road, Near ISCON Temple, Juhu, Mumbai and the average price for two people is Rs.400\nFuel Up (rated 3.9) in 7, New Shantivan Building, Oberoi Complex Road, Sab TV Lane, Andheri Lokhandwala, Andheri West, Mumbai and the average price for two people is Rs.450\nSquares Pizza And Cafe (rated 3.7) in Unit K 17, Sonal Heavy Industrial Estate, Ramchandra Lane Extension, Link Road, Malad West, Mumbai and the average price for two people is Rs.550\nJoe's Pizza (rated 3.6) in Shop 7, Plot 431, Katra Bhavan, 15th Road, Bandra, Khar West, Mumbai and the average price for two people is Rs.500\n"}
    - utter_ask_email
* send_email{"email": "asffdggfg@gmail.com"}
    - slot{"email": "asffdggfg@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
   
    

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"location": "bengaluru"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\nByg Brewski Brewing Company in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore has been rated 4.9\n\nByg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore has been rated 4.9\n\nBrahma Brews in 24th Main, 7th Phase, Opposite Brigade Palm Springs, JP Nagar, Bangalore has been rated 4.9\n\nTBC- Sky Lounge in 36/1, 5th Floor, Berry's Hotel, Kadubeesanahalli, Opposite JP Morgan, Ring Road, Marathahalli, Bangalore has been rated 4.9\n\nTBC Sky Lounge in Astra Hotel, 2795, 27th Main, Sector 1, HSR, Bangalore has been rated 4.9\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \nByg Brewski Brewing Company in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore has been rated - 4.9 and has average price for two people - Rs.1600\nByg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore has been rated - 4.9 and has average price for two people - Rs.1600\nBrahma Brews in 24th Main, 7th Phase, Opposite Brigade Palm Springs, JP Nagar, Bangalore has been rated - 4.9 and has average price for two people - Rs.1850\nTBC- Sky Lounge in 36/1, 5th Floor, Berry's Hotel, Kadubeesanahalli, Opposite JP Morgan, Ring Road, Marathahalli, Bangalore has been rated - 4.9 and has average price for two people - Rs.1600\nTBC Sky Lounge in Astra Hotel, 2795, 27th Main, Sector 1, HSR, Bangalore has been rated - 4.9 and has average price for two people - Rs.1600\nBarbeque Nation in 4005, HAL 2nd Stage, 100 Feet Road, Indiranagar, Bangalore has been rated - 4.9 and has average price for two people - Rs.1600\nBiergarten in 2, Doddanekkundi, Whitefield Road, Mahadevpura, Whitefield, Bangalore has been rated - 4.9 and has average price for two people - Rs.2400\nUDP Urban Deccan Pub in 4032, 100 Feet Road, HAL 2nd Stage, Near Domlur Bridge, Indiranagar, Bangalore has been rated - 4.9 and has average price for two people - Rs.1400\nStreet Storyss in Srinivasan Towers, ESI Hospital Road, Indiranagar, Bangalore has been rated - 4.8 and has average price for two people - Rs.1300\nBiergarten in 4th B Cross, Koramangala 5th Block, Bangalore has been rated - 4.8 and has average price for two people - Rs.2600\nThanks,\n"}
    - utter_ask_email
* send_email{"email": "jainsiris1h@rediffmail.com"}
    - slot{"email": "jainsiris1h@rediffmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\nAB's - Absolute Barbecues in T-02, 3rd Floor, Inorbit Mall, Mind Space Road, Hitech City, Hyderabad has been rated 4.9\n\nSahib’s Barbeque by Ohri’s in Ohris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur has been rated 4.9\n\nThe Roastery Coffee House in 8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad has been rated 4.8\n\nChina Bistro in 1st Floor, Signature Towers, Opposite Botanical Garden, Kondapur, Hyderabad has been rated 4.8\n\nOhri's Tansen in Ohri's at Jalavihar, Beside Jalvihar Entertainment Private Limited, Necklace Road, Hyderabad has been rated 4.7\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \nAB's - Absolute Barbecues in T-02, 3rd Floor, Inorbit Mall, Mind Space Road, Hitech City, Hyderabad has been rated - 4.9 and has average price for two people - Rs.1200\nSahib’s Barbeque by Ohri’s in Ohris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur has been rated - 4.9 and has average price for two people - Rs.1400\nThe Roastery Coffee House in 8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad has been rated - 4.8 and has average price for two people - Rs.800\nChina Bistro in 1st Floor, Signature Towers, Opposite Botanical Garden, Kondapur, Hyderabad has been rated - 4.8 and has average price for two people - Rs.1600\nOhri's Tansen in Ohri's at Jalavihar, Beside Jalvihar Entertainment Private Limited, Necklace Road, Hyderabad has been rated - 4.7 and has average price for two people - Rs.1500\nParadise Biryani in SD Road, Paradise Circle, Secunderabad has been rated - 4.7 and has average price for two people - Rs.800\nCarpe Diem in 724/A, Road 37, Jubilee Hills, Hyderabad has been rated - 4.6 and has average price for two people - Rs.2000\nParadise Biryani in Plot 22-23, Vinayaknagar, Gachibowli Main Road, Gachibowli, Hyderabad has been rated - 4.6 and has average price for two people - Rs.800\nUnited Kitchens of India in The Purple Leaf Hotel, 3-7-218, Ground Floor, Karkhana Road, Karkhana, Secunderabad has been rated - 4.6 and has average price for two people - Rs.1000\nMandil in 1-90/7/B/22, 8, 9, Cyber Enclave, Opposite Trident Hotel, Hitech City, Hyderabad has been rated - 4.6 and has average price for two people - Rs.750\nThanks,\n"}
    - utter_ask_email
* send_email{"email": "jainsirish@rediffmail.com"}
    - slot{"email": "jainsirish@rediffmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye





## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location": "Chennai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\nShree Mithai in 18, Dr TV Road, Chetpet, Chennai has been rated 4.6\n\nV4 Midnight Dhabba in 16, 2nd Floor, Rajee Complex, CTH Main Road, Near Vivekanandha School, Ambattur, Chennai has been rated 4.5\n\nWelcome Hotel in 112/241, Purasawalkam High Road, Purasavakkam, Chennai. has been rated 4.5\n\nYaa Mohaideen Briyani in 336 & 338, Main Road, Pallavaram, Chennai has been rated 4.4\n\nSS Hyderabad Biryani in 98/339, Arcot Road, Opposite Gokulam Chit Funds, Kodambakkam, Chennai has been rated 4.4\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \nShree Mithai in 18, Dr TV Road, Chetpet, Chennai has been rated - 4.6 and has average price for two people - Rs.300\nV4 Midnight Dhabba in 16, 2nd Floor, Rajee Complex, CTH Main Road, Near Vivekanandha School, Ambattur, Chennai has been rated - 4.5 and has average price for two people - Rs.600\nWelcome Hotel in 112/241, Purasawalkam High Road, Purasavakkam, Chennai. has been rated - 4.5 and has average price for two people - Rs.300\nYaa Mohaideen Briyani in 336 & 338, Main Road, Pallavaram, Chennai has been rated - 4.4 and has average price for two people - Rs.500\nSS Hyderabad Biryani in 98/339, Arcot Road, Opposite Gokulam Chit Funds, Kodambakkam, Chennai has been rated - 4.4 and has average price for two people - Rs.500\nV4 Midnight Dhabba in 22, Nolambur Service Road, Opposite KG Signature City, Mogappair West, Chennai has been rated - 4.4 and has average price for two people - Rs.550\nYaa Mohaideen Biryani in 4/158, Church Road, Opposite Uzhavar Santhai & Tea Stall, Pallavaram, Chennai has been rated - 4.4 and has average price for two people - Rs.600\nShree Mithai in 189, AI Block, Shanthi Colony, Anna Nagar East, Chennai has been rated - 4.4 and has average price for two people - Rs.300\nKrishna's Dosa Kadai in 40, Nolambur, Phase - 1, Mogappair, Chennai has been rated - 4.3 and has average price for two people - Rs.350\nSS Hyderabad Biryani in 109, Valluvarkottam High Road, Nungambakkam, Chennai has been rated - 4.3 and has average price for two people - Rs.500\nThanks,\n"}
    - utter_ask_email
* send_email{"email": "jgfkghfn13@gmail.com"}
    - slot{"email": "jgfkghfn13@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_check_location
    - slot{"location": "gurgaon"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\nIndian Accent in The Lodhi, Lodhi Road, New Delhi has been rated 4.9\n\nHauz Khas Social in 9-A & 12, Hauz Khas Village, New Delhi has been rated 4.8\n\nAh So Yum in Plot 679, Saraswati Kunj, Sector 53, Golf Course Road, Gurgaon has been rated 4.8\n\nDoodle's Garden in Plot 1, 2nd Floor, NWA Club Road, Punjabi Bagh, New Delhi has been rated 4.8\n\nGastronomica Kitchen & Bar in M-55, 2nd Floor, M Block Market, Greater Kailash 1 (GK 1), New Delhi has been rated 4.7\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \nIndian Accent in The Lodhi, Lodhi Road, New Delhi has been rated - 4.9 and has average price for two people - Rs.5000\nHauz Khas Social in 9-A & 12, Hauz Khas Village, New Delhi has been rated - 4.8 and has average price for two people - Rs.1300\nAh So Yum in Plot 679, Saraswati Kunj, Sector 53, Golf Course Road, Gurgaon has been rated - 4.8 and has average price for two people - Rs.1400\nDoodle's Garden in Plot 1, 2nd Floor, NWA Club Road, Punjabi Bagh, New Delhi has been rated - 4.8 and has average price for two people - Rs.1800\nGastronomica Kitchen & Bar in M-55, 2nd Floor, M Block Market, Greater Kailash 1 (GK 1), New Delhi has been rated - 4.7 and has average price for two people - Rs.2300\nIndian Grill Room in 315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon has been rated - 4.7 and has average price for two people - Rs.1800\nMaster Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated - 4.7 and has average price for two people - Rs.1800\nNona's Kitchen in A 224, Ground Floor, Supermart 1, DLF Phase 4, Gurgaon has been rated - 4.7 and has average price for two people - Rs.1000\nOdeon Social in 23, 1st Floor, Odeon Building, Radial 5, D Block, Connaught Place, New Delhi has been rated - 4.7 and has average price for two people - Rs.1300\nCafe Wink in G-1, Plot 9, Sikka Galaxy, Shreshtha Vihar, Anand Vihar, New Delhi has been rated - 4.6 and has average price for two people - Rs.800\nThanks,\n"}
    - utter_ask_email
* send_email{"email": "jainsirish@rediffmail.com"}
    - slot{"email": "jainsirish@rediffmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Meerut"}
    - slot{"location": "Meerut"}
    - action_check_location
    - slot{"location": "Meerut"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. The Yellow Chilli in 267/1 - 269/1, Mangel Pandey Nagar, Shastri Nagar, Meerut has been rated 4.7\n\n2. Barbeque Nation in 3rd Floor, Khasra No 5832, Pinnacle Tower, Garh Rd, Panchsheel Colony, Meerut, Uttar Pradesh 250003 has been rated 4.7\n\n3. Meera's Bistro in Main Road, NH 58, Village Nagla Tashi, Pallavpuram, Meerut has been rated 4.5\n\n4. Villa 183 in Shop 183, Abu Lane, Sadar Bazaar, Meerut has been rated 4.2\n\n5. Tandoori Club in 18, First Floor, B 5, Purwa Jugal Kishore Delhi Road, Near Metro Plaza, Devpuri, Meerut has been rated 3.9\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. The Yellow Chilli in 267/1 - 269/1, Mangel Pandey Nagar, Shastri Nagar, Meerut has been rated - 4.7 and has average price for two people - Rs.1000\n2. Barbeque Nation in 3rd Floor, Khasra No 5832, Pinnacle Tower, Garh Rd, Panchsheel Colony, Meerut, Uttar Pradesh 250003 has been rated - 4.7 and has average price for two people - Rs.1200\n3. Meera's Bistro in Main Road, NH 58, Village Nagla Tashi, Pallavpuram, Meerut has been rated - 4.5 and has average price for two people - Rs.800\n4. Villa 183 in Shop 183, Abu Lane, Sadar Bazaar, Meerut has been rated - 4.2 and has average price for two people - Rs.950\n5. Tandoori Club in 18, First Floor, B 5, Purwa Jugal Kishore Delhi Road, Near Metro Plaza, Devpuri, Meerut has been rated - 3.9 and has average price for two people - Rs.700\n6. Olivia in 183-D, Civil Lines, Boundary Road, Meerut Cantt, Meerut has been rated - 3.7 and has average price for two people - Rs.1000\n7. Chakhna Restaurant & Lounge in Shop 7, Lakhpat Building, Begum Bridge Road, Meerut Cantt, Meerut has been rated - 3.6 and has average price for two people - Rs.800\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* send_email{"email": "jai.jfgf@gmail.com"}
    - slot{"email": "jai.jfgf@gmail.com"}
    - action_send_email
    - slot{"email": "jai.jfgf@gmail.com"}
* goodbye
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Udaipur"}
    - slot{"location": "Udaipur"}
    - action_check_location
    - slot{"location_found": "tier3"}
    - utter_don't_work_city
* affirm{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\nAB's - Absolute Barbecues in T-02, 3rd Floor, Inorbit Mall, Mind Space Road, Hitech City, Hyderabad has been rated 4.9\n\nSahib’s Barbeque by Ohri’s in Ohris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur has been rated 4.9\n\nThe Roastery Coffee House in 8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad has been rated 4.8\n\nChina Bistro in 1st Floor, Signature Towers, Opposite Botanical Garden, Kondapur, Hyderabad has been rated 4.8\n\nOhri's Tansen in Ohri's at Jalavihar, Beside Jalvihar Entertainment Private Limited, Necklace Road, Hyderabad has been rated 4.7\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \nAB's - Absolute Barbecues in T-02, 3rd Floor, Inorbit Mall, Mind Space Road, Hitech City, Hyderabad has been rated - 4.9 and has average price for two people - Rs.1200\nSahib’s Barbeque by Ohri’s in Ohris Cyber Grub, Plot 4/1 & 4/2, 64, Huda Techno Enclave, Mind Space Centre, Madhapur has been rated - 4.9 and has average price for two people - Rs.1400\nThe Roastery Coffee House in 8/2/287/12, House 418, Road 14, Banjara Hills, Hyderabad has been rated - 4.8 and has average price for two people - Rs.800\nChina Bistro in 1st Floor, Signature Towers, Opposite Botanical Garden, Kondapur, Hyderabad has been rated - 4.8 and has average price for two people - Rs.1600\nOhri's Tansen in Ohri's at Jalavihar, Beside Jalvihar Entertainment Private Limited, Necklace Road, Hyderabad has been rated - 4.7 and has average price for two people - Rs.1500\nParadise Biryani in SD Road, Paradise Circle, Secunderabad has been rated - 4.7 and has average price for two people - Rs.800\nCarpe Diem in 724/A, Road 37, Jubilee Hills, Hyderabad has been rated - 4.6 and has average price for two people - Rs.2000\nParadise Biryani in Plot 22-23, Vinayaknagar, Gachibowli Main Road, Gachibowli, Hyderabad has been rated - 4.6 and has average price for two people - Rs.800\nUnited Kitchens of India in The Purple Leaf Hotel, 3-7-218, Ground Floor, Karkhana Road, Karkhana, Secunderabad has been rated - 4.6 and has average price for two people - Rs.1000\nMandil in 1-90/7/B/22, 8, 9, Cyber Enclave, Opposite Trident Hotel, Hitech City, Hyderabad has been rated - 4.6 and has average price for two people - Rs.750\nThanks,\n"}
    - utter_ask_email
* send_email{"email": "jainsirish@rediffmail.com"}
    - slot{"email": "jainsirish@rediffmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Solapur"}
    - slot{"location": "Solapur"}
    - action_check_location
    - slot{"location": "Solapur"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_pricerange
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Hotel Bhaijaan in CTS 201/1, Shop 2, 3, 4, 7, Krushan Plaza, Hotgi Road, Solapur Locality, Solapur has been rated 4.5\n\n2. Hotel Angraj Pure Veg in 1012/1014 North Kasba, Solapur - 413001, Near Uapase Hospital, Balives, Solapur Locality, Solapur has been rated 4.5\n\n3. Juice Galaxy in Laxmi Villa, Gandhi Nagar Chowk, Near Heritage Garden, Solapur Locality, Solapur has been rated 4.4\n\n4. Laziz Pizza in Block 4, A Sanmati Nagar, Vijapur Road, Solapur Locality, Solapur has been rated 4.4\n\n5. Chicken Factory in 98 Railway lines Near Mayor Bungalow Railway Lines Solapur , Solapur, Solapur has been rated 4.3\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Hotel Bhaijaan in CTS 201/1, Shop 2, 3, 4, 7, Krushan Plaza, Hotgi Road, Solapur Locality, Solapur has been rated - 4.5 and has average price for two people - Rs.400\n2. Hotel Angraj Pure Veg in 1012/1014 North Kasba, Solapur - 413001, Near Uapase Hospital, Balives, Solapur Locality, Solapur has been rated - 4.5 and has average price for two people - Rs.400\n3. Juice Galaxy in Laxmi Villa, Gandhi Nagar Chowk, Near Heritage Garden, Solapur Locality, Solapur has been rated - 4.4 and has average price for two people - Rs.400\n4. Laziz Pizza in Block 4, A Sanmati Nagar, Vijapur Road, Solapur Locality, Solapur has been rated - 4.4 and has average price for two people - Rs.300\n5. Chicken Factory in 98 Railway lines Near Mayor Bungalow Railway Lines Solapur , Solapur, Solapur has been rated - 4.3 and has average price for two people - Rs.350\n6. Hotel Yash Palace in 69 Castle Apartment, Station Road, Solapur - 413001, Opp Mahapaur Banglow, Solapur Locality, Solapur has been rated - 4.3 and has average price for two people - Rs.400\n7. Hotel Ajinkya in 131, Solapur - 413001, Murarji Peth Lucky Chowk, Solapur Locality, Solapur has been rated - 4.3 and has average price for two people - Rs.400\n8. Hotel Priyanka in 131, Siddheshwar Peth, Civil Chowk, Solapur Locality, Solapur has been rated - 4.2 and has average price for two people - Rs.500\n9. McDonald's in Shop No 1 Ground Floor Oasis Mall, Muraraji Peth, Solapur - 413002, Near Meena Theatre Near Ajantha Ladge Mechanical Chowk, Solapur Locality, Solapur has been rated - 4.2 and has average price for two people - Rs.300\n10. Hotel Mantralaya in 8389/3, BNR Jawahar Appartment 162, Railway Line, Solapur Locality, Solapur has been rated - 4.2 and has average price for two people - Rs.300\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* send_email{"email": "134jaifdghfhljf@fhgf13.co.in"}
    - slot{"email": "134jaifdghfhljf@fhgf13.co.in"}
    - action_send_email
    - slot{"email": "134jaifdghfhljf@fhgf13.co.in"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Bhopal"}
    - slot{"location": "Bhopal"}
    - action_check_location
    - slot{"location": "Bhopal"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Sagar Gaire Fast Food : Arera Colony in 10, Number Market, Arera Colony, Bhopal has been rated 4.6\n\n2. Sagar Gaire Fast Food : Platinum Plaza in Shop  33-34,Ground Floor, Platinum Plaza, TT Nagar, Bhopal has been rated 4.5\n\n3. Sagar Gaire Fast Food : 7 Number in Shop 101, B.D.A Complex, Habib Ganj, Bhopal has been rated 4.4\n\n4. Anni Bhai ki Biryani in Shop 1, Qazi Camp, Next to Taj Studio, JP Nagar, Bhopal has been rated 4.4\n\n5. Sagar Gaire Fast Food : Bhawani Dham in 13, Bhawani Dham, Jai Durga Nagar Gram, Narela Sankari, Ayodhya Bypass Road, BHEL, Bhopal has been rated 4.3\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Sagar Gaire Fast Food : Arera Colony in 10, Number Market, Arera Colony, Bhopal has been rated - 4.6 and has average price for two people - Rs.250\n2. Sagar Gaire Fast Food : Platinum Plaza in Shop  33-34,Ground Floor, Platinum Plaza, TT Nagar, Bhopal has been rated - 4.5 and has average price for two people - Rs.250\n3. Sagar Gaire Fast Food : 7 Number in Shop 101, B.D.A Complex, Habib Ganj, Bhopal has been rated - 4.4 and has average price for two people - Rs.250\n4. Anni Bhai ki Biryani in Shop 1, Qazi Camp, Next to Taj Studio, JP Nagar, Bhopal has been rated - 4.4 and has average price for two people - Rs.250\n5. Sagar Gaire Fast Food : Bhawani Dham in 13, Bhawani Dham, Jai Durga Nagar Gram, Narela Sankari, Ayodhya Bypass Road, BHEL, Bhopal has been rated - 4.3 and has average price for two people - Rs.250\n6. Haji Hotel in House 13, Madina Hotel Gali Ibrahimpura, Peer Gate Area, Bhopal has been rated - 4.3 and has average price for two people - Rs.200\n7. Alfry Foods in Shop 18, Masjid Umrao Dulha, Peer Gate Area, Bhopal has been rated - 4.3 and has average price for two people - Rs.250\n8. Rafiq Biryaan in Shop 369, Gali 3, Qazi Camp Congress, Opposite Taj Studio, JP Nagar, Bhopal has been rated - 4.3 and has average price for two people - Rs.200\n9. Sagar Gaire Fast Food - Idgah Hills in Shop 1, 2, 3, Meenakshi Complex, Aali Manzil Road, Niyamatpura, Idgah Hills, Bhopal has been rated - 4.2 and has average price for two people - Rs.250\n10. Al-Beik in Plot 9, Shop 7, Ram Gopal Maheshwari Marg, Zone 1, Maharana Pratap Nagar, Bhopal has been rated - 4.2 and has average price for two people - Rs.200\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* send_email{"email": "jaisnighgfj@yahoo.co.in"}
    - slot{"email": "jaisnighgfj@yahoo.co.in"}
    - action_send_email
    - slot{"email": "jaisnighgfj@yahoo.co.in"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - action_check_location
    - slot{"location": "Chandigarh"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_pricerange
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Sandhya in Booth 37 & 40, Rehri Market, Sector 7, Panchkula has been rated 3.9\n\n2. Jalandhar Sweets in 15-18, Sector 23 C, Near Sector 23, Chandigarh has been rated 3.9\n\n3. Red Chilli in Shop 2, House 1420/1, Sai PG, Adarsh Nagar, Kharar, Sas Nagar, Nayagaon, Nayagaon has been rated 3.5\n\n4. Roll Masters in Shop 14, Cabin 2, Near Bus Stand, Kharar Road, Mohali has been rated 3.4\n\n5. Momo House in Shop 17, Zimidara Enclave 1, Patiala Road, Utrathiya, Zirakpur has been rated 3.3\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Sandhya in Booth 37 & 40, Rehri Market, Sector 7, Panchkula has been rated - 3.9 and has average price for two people - Rs.250\n2. Jalandhar Sweets in 15-18, Sector 23 C, Near Sector 23, Chandigarh has been rated - 3.9 and has average price for two people - Rs.250\n3. Red Chilli in Shop 2, House 1420/1, Sai PG, Adarsh Nagar, Kharar, Sas Nagar, Nayagaon, Nayagaon has been rated - 3.5 and has average price for two people - Rs.200\n4. Roll Masters in Shop 14, Cabin 2, Near Bus Stand, Kharar Road, Mohali has been rated - 3.4 and has average price for two people - Rs.250\n5. Momo House in Shop 17, Zimidara Enclave 1, Patiala Road, Utrathiya, Zirakpur has been rated - 3.3 and has average price for two people - Rs.100\n6. Uttrakhand Momos in 21/22, Dashmesh Nagar, Defence Colony, Utrathiya, Zirakpur has been rated - 3.0 and has average price for two people - Rs.200\n7. PB 70 Food Corner in SCO 1, Paras Bank Square, Ambala Chandigarh Highway, Dera Bassi, Zirakpur has been rated - 3.0 and has average price for two people - Rs.250\n8. Rajan Food Corner in Garja Complex, Adarsh Nagar, Nayagaon has been rated - 2.9 and has average price for two people - Rs.250\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* send_email{"email": "jainsirish@rediffmail.com"}
    - slot{"email": "jainsirish@rediffmail.com"}
    - action_send_email
    - slot{"email": "jainsirish@rediffmail.com"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bijapur"}
    - slot{"location": "Bijapur"}
    - action_check_location
    - slot{"location": "Bijapur"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Anna Idli in Mela Shankar Complex, Ram Mandir Road, Vijaypura, Bijapur has been rated 4.2\n\n2. Hotel Lalit Mahal in Near Bus stand Vijapur Bijapur, Bijapur Locality, Bijapur has been rated 4.1\n\n3. Shrinidhi Hotel in WN No. 4, Oppo Engineering College Ashram Road, Vijayapura, Bijapur, Bijapur Locality, Bijapur has been rated 4.0\n\n4. OYALO in Plot No.162, Near BDA Garden, Vivek Nagar, Vijayapur, Bijapur Locality, Bijapur has been rated 3.9\n\n5. Hotel Shri Sai Garden in Near BLD Engineering college, Ashram Road, Vijayapur Bijapur, Bijapur Locality, Bijapur has been rated 3.9\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Anna Idli in Mela Shankar Complex, Ram Mandir Road, Vijaypura, Bijapur has been rated - 4.2 and has average price for two people - Rs.200\n2. Hotel Lalit Mahal in Near Bus stand Vijapur Bijapur, Bijapur Locality, Bijapur has been rated - 4.1 and has average price for two people - Rs.200\n3. Shrinidhi Hotel in WN No. 4, Oppo Engineering College Ashram Road, Vijayapura, Bijapur, Bijapur Locality, Bijapur has been rated - 4.0 and has average price for two people - Rs.200\n4. OYALO in Plot No.162, Near BDA Garden, Vivek Nagar, Vijayapur, Bijapur Locality, Bijapur has been rated - 3.9 and has average price for two people - Rs.150\n5. Hotel Shri Sai Garden in Near BLD Engineering college, Ashram Road, Vijayapur Bijapur, Bijapur Locality, Bijapur has been rated - 3.9 and has average price for two people - Rs.200\n6. Halli Mane in Station Road Bijapur, Bijapur Locality, Bijapur has been rated - 3.9 and has average price for two people - Rs.200\n7. Five Star Chicken in Bagalkot Cross Vijayapur Bijapur, Bijapur Locality, Bijapur has been rated - 3.7 and has average price for two people - Rs.200\n8. 7th Wonder in Jorapur Layout, Banjara Cross, Vijayapur, Bijapur Locality, Bijapur has been rated - 3.7 and has average price for two people - Rs.200\n9. Baskin Robbins in Shop 302, Third Floor, Patil Planet Mall, Near Banjara Cross, Bijapur Locality, Bijapur has been rated - 3.7 and has average price for two people - Rs.200\n10. Dhaneshwari Padd Center in Near TST Talkies, M.G Road VIJAYAPUR, Bijapur, Bijapur, Karnataka, Bijapur Locality, Bijapur has been rated - 3.7 and has average price for two people - Rs.150\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* send_email{"email": "jainsirish@edu.co"}
    - slot{"email": "jainsirish@edu.co"}
    - action_send_email
    - slot{"email": "jainsirish@edu.co"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location_found": "tier3"}
* restaurant_search{"location": "Allahabad"}
    - slot{"location": "Allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. EDEN by Connoisseur in Hotel Samrat, Civil Lines, Allahabad has been rated 4.9\n\n2. Sagar Ratna in 3/3, Hashimpur Road, Balson Crossing, Near Anand Bhawan, Tagore Town, Allahabad has been rated 4.5\n\n3. Old School Cafe in 2nd Floor, 9-10 Tulsiani Grace, Civil Lines, Allahabad has been rated 4.4\n\n4. El Chico Restaurant in 142A, 32, Mahatma Gandhi, Civil Lines, Allahabad has been rated 4.4\n\n5. Pind Balluchi in 48/8, Stratchy Road, Civil Lines, Allahabad has been rated 4.3\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. EDEN by Connoisseur in Hotel Samrat, Civil Lines, Allahabad has been rated - 4.9 and has average price for two people - Rs.1000\n2. Sagar Ratna in 3/3, Hashimpur Road, Balson Crossing, Near Anand Bhawan, Tagore Town, Allahabad has been rated - 4.5 and has average price for two people - Rs.800\n3. Old School Cafe in 2nd Floor, 9-10 Tulsiani Grace, Civil Lines, Allahabad has been rated - 4.4 and has average price for two people - Rs.1000\n4. El Chico Restaurant in 142A, 32, Mahatma Gandhi, Civil Lines, Allahabad has been rated - 4.4 and has average price for two people - Rs.800\n5. Pind Balluchi in 48/8, Stratchy Road, Civil Lines, Allahabad has been rated - 4.3 and has average price for two people - Rs.1000\n6. Berco's in 17C, 0-1, Stretchy Road, Civil Lines, Allahabad has been rated - 4.2 and has average price for two people - Rs.1600\n7. Makkhan's in 8, 9 Tulsiani Grace, 25 Edmonston Road, Civil Lines, Allahabad has been rated - 4.2 and has average price for two people - Rs.1000\n8. Moti Mahal Delux in Second Floor, Vinayak City Center Mall, SP Marg, Civil Lines, Allahabad has been rated - 4.1 and has average price for two people - Rs.850\n9. Relish Restaurant- The Legend Hotel in The Legend Hotel, First Floor, 23 C, Thornhill Road, Civil Lines, Allahabad has been rated - 4.0 and has average price for two people - Rs.1100\n10. Jade Garden in 123/27A, MG Marg, Civil Lines, Allahabad has been rated - 4.0 and has average price for two people - Rs.800\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* send_email{"email": "hanifkhan.86@gmail.com"}
    - slot{"email": "hanifkhan.86@gmail.com"}
    - action_send_email
    - slot{"email": "hanifkhan.86@gmail.com"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location": "Kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_pricerange
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Al Baik Fast Food Corner in 54, Phears Lane, Bara Bazar, Kolkata has been rated 3.8\n\n2. Abar Khaboo in 26/42, Dum Dum Road, Near Chiria More, Paikpara, Kolkata has been rated 3.8\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Al Baik Fast Food Corner in 54, Phears Lane, Bara Bazar, Kolkata has been rated - 3.8 and has average price for two people - Rs.250\n2. Abar Khaboo in 26/42, Dum Dum Road, Near Chiria More, Paikpara, Kolkata has been rated - 3.8 and has average price for two people - Rs.250\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* affirm
    - utter_affirm
* send_email{"email": "hanifkhan.86@gmail.com"}
    - slot{"email": "hanifkhan.86@gmail.com"}
    - action_send_email
    - slot{"email": "hanifkhan.86@gmail.com"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_default
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_pricerange
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": "found"}
    - utter_ask_pricerange
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Sandhya in Booth 37 & 40, Rehri Market, Sector 7, Panchkula has been rated 3.9\n\n2. Jalandhar Sweets in 15-18, Sector 23 C, Near Sector 23, Chandigarh has been rated 3.9\n\n3. Red Chilli in Shop 2, House 1420/1, Sai PG, Adarsh Nagar, Kharar, Sas Nagar, Nayagaon, Nayagaon has been rated 3.5\n\n4. Roll Masters in Shop 14, Cabin 2, Near Bus Stand, Kharar Road, Mohali has been rated 3.4\n\n5. Momo House in Shop 17, Zimidara Enclave 1, Patiala Road, Utrathiya, Zirakpur has been rated 3.3\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Sandhya in Booth 37 & 40, Rehri Market, Sector 7, Panchkula has been rated - 3.9 and has average price for two people - Rs.250\n2. Jalandhar Sweets in 15-18, Sector 23 C, Near Sector 23, Chandigarh has been rated - 3.9 and has average price for two people - Rs.250\n3. Red Chilli in Shop 2, House 1420/1, Sai PG, Adarsh Nagar, Kharar, Sas Nagar, Nayagaon, Nayagaon has been rated - 3.5 and has average price for two people - Rs.200\n4. Roll Masters in Shop 14, Cabin 2, Near Bus Stand, Kharar Road, Mohali has been rated - 3.4 and has average price for two people - Rs.250\n5. Momo House in Shop 17, Zimidara Enclave 1, Patiala Road, Utrathiya, Zirakpur has been rated - 3.3 and has average price for two people - Rs.100\n6. Uttrakhand Momos in 21/22, Dashmesh Nagar, Defence Colony, Utrathiya, Zirakpur has been rated - 3.0 and has average price for two people - Rs.200\n7. PB 70 Food Corner in SCO 1, Paras Bank Square, Ambala Chandigarh Highway, Dera Bassi, Zirakpur has been rated - 3.0 and has average price for two people - Rs.250\n8. Rajan Food Corner in Garja Complex, Adarsh Nagar, Nayagaon has been rated - 2.9 and has average price for two people - Rs.250\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* negative
    - utter_negative
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_location
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_pricerange
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. ABAOTIME in Ground Floor, Accord Bleu, Kavuri Hills Phase 1, Madhapur, Hyderabad has been rated 4.6\n\n2. Fully Fed Up in Plot 23, Hi-Tension Road, Eshwarpuri Colony, Sainikpuri, Secunderabad has been rated 4.2\n\n3. Chop Sticks in 8-3-960/9, Srinagar Colony, Hyderabad has been rated 4.1\n\n4. Dusk 2 Dawn in The Alley, Image Hospital Lane, Near Venkateshwara College, Madhapur, Hyderabad has been rated 4.1\n\n5. Kim Fung in Opposite NIN Bus Stop, Vijayapuri Colony, Lalaguda Road, Tarnaka, Hyderabad has been rated 4.1\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. ABAOTIME in Ground Floor, Accord Bleu, Kavuri Hills Phase 1, Madhapur, Hyderabad has been rated - 4.6 and has average price for two people - Rs.500\n2. Fully Fed Up in Plot 23, Hi-Tension Road, Eshwarpuri Colony, Sainikpuri, Secunderabad has been rated - 4.2 and has average price for two people - Rs.500\n3. Chop Sticks in 8-3-960/9, Srinagar Colony, Hyderabad has been rated - 4.1 and has average price for two people - Rs.300\n4. Dusk 2 Dawn in The Alley, Image Hospital Lane, Near Venkateshwara College, Madhapur, Hyderabad has been rated - 4.1 and has average price for two people - Rs.450\n5. Kim Fung in Opposite NIN Bus Stop, Vijayapuri Colony, Lalaguda Road, Tarnaka, Hyderabad has been rated - 4.1 and has average price for two people - Rs.500\n6. Chin Ling in 9-1-94/A, Near Sangeet Theatre, S D Road, Secunderabad has been rated - 4.1 and has average price for two people - Rs.400\n7. Chopsuey Kitchen in A13, KitchD Foodcourt, Near BRC Infra Apartment, Puppalguda, Manikonda, Hyderabad has been rated - 4.1 and has average price for two people - Rs.400\n8. Chinese World in Beside Traffic Police Station, Near IMAX, Necklace Road, Hyderabad has been rated - 4.1 and has average price for two people - Rs.300\n9. Alex's Kitchen in 3-6-10, Liberty Road, Himayath Nagar, Hyderabad has been rated - 4.0 and has average price for two people - Rs.600\n10. Eats Corner in Shop 5, Plot 31, B Block, Sri Ram Nagar, Near Sri Krishna Veni Talent School, Botanical Garden Road, Kondapur, Hyderabad has been rated - 4.0 and has average price for two people - Rs.400\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* negative
    - utter_negative
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Cuttack"}
    - slot{"location": "Cuttack"}
    - action_check_location
    - slot{"location_found": "notfound"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - action_check_location
    - slot{"location": "cuttack"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Burger Adda Factory in Near Basundhara Lane, Ward 5, Bidanasi, Cuttack has been rated 3.9\n\n2. Biriyani Box in Near General Post Office, Buxi Bazaar, Cuttack has been rated 3.7\n\n3. Damas Food Junction in C-1112, Sector 6, CDA Sector 6, Cuttack has been rated 3.7\n\n4. U Me Aur Hum in Manik Gosh Bazar, Near Sri Rani Satiji Mandir, Buxi Bazaar, Cuttack has been rated 3.7\n\n5. Kaffe Delite in Deulasahi Chak, Infront Of Sri Guru Mistan Bhandar, Bidanasi, Cuttack has been rated 3.7\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Burger Adda Factory in Near Basundhara Lane, Ward 5, Bidanasi, Cuttack has been rated - 3.9 and has average price for two people - Rs.250\n2. Biriyani Box in Near General Post Office, Buxi Bazaar, Cuttack has been rated - 3.7 and has average price for two people - Rs.200\n3. Damas Food Junction in C-1112, Sector 6, CDA Sector 6, Cuttack has been rated - 3.7 and has average price for two people - Rs.200\n4. U Me Aur Hum in Manik Gosh Bazar, Near Sri Rani Satiji Mandir, Buxi Bazaar, Cuttack has been rated - 3.7 and has average price for two people - Rs.100\n5. Kaffe Delite in Deulasahi Chak, Infront Of Sri Guru Mistan Bhandar, Bidanasi, Cuttack has been rated - 3.7 and has average price for two people - Rs.250\n6. Hotel Asha in Haripur Road, Siba Bazaar, Cuttack has been rated - 3.6 and has average price for two people - Rs.250\n7. Jagadamba Fast Food and Restaurant in Aparna Nagar, Chauliaganj, Naya Bazaar, Cuttack has been rated - 3.6 and has average price for two people - Rs.250\n8. Dama Maharaj Sweets in Near GPO, Buxi Bazaar, Cuttack has been rated - 3.6 and has average price for two people - Rs.100\n9. Hotel Punjabi Tadka in Biju Pattnaik Square, Police Colony has been rated - 3.6 and has average price for two people - Rs.250\n10. Bobaalo in Truck Number-2, Infront of Paris Bakery, CDA Sector 10, Cuttack, CDA Sector 6, Cuttack has been rated - 3.6 and has average price for two people - Rs.250\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* negative
    - utter_negative
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Indian Accent in The Lodhi, Lodhi Road, New Delhi has been rated 4.9\n\n2. Hauz Khas Social in 9-A & 12, Hauz Khas Village, New Delhi has been rated 4.8\n\n3. Hauz Khas Social in 9-A & 12, Hauz Khas Village, New Delhi has been rated 4.8\n\n4. Ah So Yum in Plot 679, Saraswati Kunj, Sector 53, Golf Course Road, Gurgaon has been rated 4.8\n\n5. Doodle's Garden in Plot 1, 2nd Floor, NWA Club Road, Punjabi Bagh, New Delhi has been rated 4.8\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Indian Accent in The Lodhi, Lodhi Road, New Delhi has been rated - 4.9 and has average price for two people - Rs.5000\n2. Hauz Khas Social in 9-A & 12, Hauz Khas Village, New Delhi has been rated - 4.8 and has average price for two people - Rs.1300\n3. Hauz Khas Social in 9-A & 12, Hauz Khas Village, New Delhi has been rated - 4.8 and has average price for two people - Rs.1300\n4. Ah So Yum in Plot 679, Saraswati Kunj, Sector 53, Golf Course Road, Gurgaon has been rated - 4.8 and has average price for two people - Rs.1400\n5. Doodle's Garden in Plot 1, 2nd Floor, NWA Club Road, Punjabi Bagh, New Delhi has been rated - 4.8 and has average price for two people - Rs.1800\n6. Indian Grill Room in 315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon has been rated - 4.7 and has average price for two people - Rs.1800\n7. Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated - 4.7 and has average price for two people - Rs.1800\n8. Daryaganj in Regal Building, Connaught Circle, Hanuman Road Area, Connaught Place, New Delhi has been rated - 4.7 and has average price for two people - Rs.1500\n9. Odeon Social in 23, 1st Floor, Odeon Building, Radial 5, D Block, Connaught Place, New Delhi has been rated - 4.7 and has average price for two people - Rs.1300\n10. C.I.A. Call it Asiian in 13/14/15/16, Narmada Shopping Complex, Opposite Don Bosco School, Alaknanda Road, Greater Kailash 2 (GK 2), New Delhi has been rated - 4.6 and has average price for two people - Rs.700\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* affirm
    - utter_affirm
* send_email{"email": "hanifkhan.86@gmail.com"}
    - slot{"email": "hanifkhan.86@gmail.com"}
    - action_send_email
    - slot{"email": "hanifkhan.86@gmail.com"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Mangalore"}
    - slot{"location": "Mangalore"}
    - action_check_location
    - slot{"location": "Mangalore"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Giri Manja's in Near Kalikamba Temple, Gopalkrishna Temple Road, Bhavathi, Mangalore Bhavathi has been rated 4.8\n\n2. Ideal Cafe in Opposite Sharavu Temple, GT Road, Hampankatta, Mangalore has been rated 4.6\n\n3. Ideal's in Ideal Building, Near Ven Lock Hospital, Market Road, Hampankatta, Mangalore has been rated 4.6\n\n4. Onesta in TF-2 & TF-3, 3rd Floor, MAK Mall, Kankanady, Mangalore has been rated 4.5\n\n5. Ideal Ice Cream Parlour in 13-2-542, GHS Road, Hampankatta, Mangalore has been rated 4.5\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Giri Manja's in Near Kalikamba Temple, Gopalkrishna Temple Road, Bhavathi, Mangalore Bhavathi has been rated - 4.8 and has average price for two people - Rs.500\n\n2. Ideal Cafe in Opposite Sharavu Temple, GT Road, Hampankatta, Mangalore has been rated - 4.6 and has average price for two people - Rs.500\n\n3. Ideal's in Ideal Building, Near Ven Lock Hospital, Market Road, Hampankatta, Mangalore has been rated - 4.6 and has average price for two people - Rs.300\n\n4. Onesta in TF-2 & TF-3, 3rd Floor, MAK Mall, Kankanady, Mangalore has been rated - 4.5 and has average price for two people - Rs.600\n\n5. Ideal Ice Cream Parlour in 13-2-542, GHS Road, Hampankatta, Mangalore has been rated - 4.5 and has average price for two people - Rs.300\n\n6. Hotel Narayana in Near Indian Overseas Bank, Azizuddin Road, Bunder, Mangalore has been rated - 4.5 and has average price for two people - Rs.300\n\n7. Waffee House in City Arcade, Bendoor, Kankanady, Mangalore has been rated - 4.4 and has average price for two people - Rs.300\n\n8. Shetty Lunch Home in Opposite Don Bosco Building, Balmatta, Mangalore has been rated - 4.4 and has average price for two people - Rs.500\n\n9. Ideal Cream Parlour in 4th Floor, City Centre Mall, KS Rao Road, KS Rao Nagar, Mangalore has been rated - 4.4 and has average price for two people - Rs.300\n\n10. Shake Factory in 36, Balmatta Road, Hampankatta, Mangaluru has been rated - 4.3 and has average price for two people - Rs.400\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* negative
    - utter_negative
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - action_check_location
    - slot{"location": "Gurgaon"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Paparizza - Lust For Crust in 2520, Hudson Lane, Delhi University-GTB Nagar, New Delhi has been rated 4.6\n\n2. China Box in 2nd Floor, Ashoka Complex, Near Ocus Quantum Mall, Sector 51, Near Sector 50, Gurgaon has been rated 4.5\n\n3. AMA Cafe in House 6, New Colony, Majnu ka Tilla, New Delhi has been rated 4.4\n\n4. Punjabi Angithi in Shop 31 & 32, DDA Market, Sector 16, Rohini, New Delhi has been rated 4.4\n\n5. Punjabi Angithi in 32-22, A 4, DDA Market, Paschim Vihar, New Delhi has been rated 4.4\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Paparizza - Lust For Crust in 2520, Hudson Lane, Delhi University-GTB Nagar, New Delhi has been rated - 4.6 and has average price for two people - Rs.500\n\n2. China Box in 2nd Floor, Ashoka Complex, Near Ocus Quantum Mall, Sector 51, Near Sector 50, Gurgaon has been rated - 4.5 and has average price for two people - Rs.600\n\n3. AMA Cafe in House 6, New Colony, Majnu ka Tilla, New Delhi has been rated - 4.4 and has average price for two people - Rs.550\n\n4. Punjabi Angithi in Shop 31 & 32, DDA Market, Sector 16, Rohini, New Delhi has been rated - 4.4 and has average price for two people - Rs.400\n\n5. Punjabi Angithi in 32-22, A 4, DDA Market, Paschim Vihar, New Delhi has been rated - 4.4 and has average price for two people - Rs.400\n\n6. Padmanabham in 52, Atul Grove Road, Opposite Metro Gate 2, Janpath, New Delhi has been rated - 4.3 and has average price for two people - Rs.600\n\n7. Punjabi Angithi in Shop 15-A, A1 Block, LSC, DDA Market, Janakpuri, New Delhi has been rated - 4.3 and has average price for two people - Rs.400\n\n8. Shake Eat Up in 2509, Ground Floor, Hudson Lane, Delhi University-GTB Nagar, New Delhi has been rated - 4.3 and has average price for two people - Rs.600\n\n9. Om Sweets & Snacks in GL-23, Hari Nagar, Jail Road, New Delhi has been rated - 4.3 and has average price for two people - Rs.500\n\n10. McDonald's in P 16, Atta Market, Sector 18, Noida has been rated - 4.2 and has average price for two people - Rs.500\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* affirm
    - utter_affirm
* send_email{"email": "hanifkhan.86@gmail.com"}
    - slot{"email": "hanifkhan.86@gmail.com"}
    - action_send_email
    - slot{"email": "hanifkhan.86@gmail.com"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_default
* restaurant_search{"cuisine": "north indian", "location": "Kolkata"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location": "Kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_pricerange
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Dehat in 104/A, Block B, Lake Town, Kolkata has been rated 3.9\n\n2. Mini Royal Cafe in 80, Bidhan Sarani, Hatibagan, Kolkata has been rated 3.8\n\n3. Pappu Biryani House in 80, Bidhan Sarani, Hatibagan, Kolkata has been rated 3.5\n\n4. Ajooba Biryani centre in 75, Ibrahimpur Road, Jadavpur, Kolkata has been rated 3.0\n\n5. Anadi Cabin in 9, Jawaharlal Nehru Road, New Market Area, Kolkata has been rated 2.8\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Dehat in 104/A, Block B, Lake Town, Kolkata has been rated - 3.9 and has average price for two people - Rs.100\n\n2. Mini Royal Cafe in 80, Bidhan Sarani, Hatibagan, Kolkata has been rated - 3.8 and has average price for two people - Rs.200\n\n3. Pappu Biryani House in 80, Bidhan Sarani, Hatibagan, Kolkata has been rated - 3.5 and has average price for two people - Rs.200\n\n4. Ajooba Biryani centre in 75, Ibrahimpur Road, Jadavpur, Kolkata has been rated - 3.0 and has average price for two people - Rs.250\n\n5. Anadi Cabin in 9, Jawaharlal Nehru Road, New Market Area, Kolkata has been rated - 2.8 and has average price for two people - Rs.150\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* negative
    - utter_negative
* goodbye
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "Aligarh"}
    - slot{"location": "Aligarh"}
    - action_check_location
    - slot{"location": "Aligarh"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. McDonalds in 3/106A - I, Ground Floor & First Floor, Hemchand Compound, Marris Road, Aligarh has been rated 4.2\n\n2. Deepak Restaurant in Tikaram Mandir Center Point Aligarh, Aligarh Locality, Aligarh has been rated 4.0\n\n3. Pie Pizza in Rifa palace, medical road, aligarh, Aligarh Locality, Aligarh has been rated 4.0\n\n4. Flamoak Cafe in Shop U-123, First Floor, Above Abhinandan Garments, Samad Road, Center Point, Aligarh Locality, Aligarh has been rated 3.9\n\n5. Family Choice Restaurant in dodhpur, civil lines Aligarh, Aligarh Locality, Aligarh has been rated 3.9\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. McDonalds in 3/106A - I, Ground Floor & First Floor, Hemchand Compound, Marris Road, Aligarh has been rated - 4.2 and has average price for two people - Rs.0\n\n2. Deepak Restaurant in Tikaram Mandir Center Point Aligarh, Aligarh Locality, Aligarh has been rated - 4.0 and has average price for two people - Rs.200\n\n3. Pie Pizza in Rifa palace, medical road, aligarh, Aligarh Locality, Aligarh has been rated - 4.0 and has average price for two people - Rs.250\n\n4. Flamoak Cafe in Shop U-123, First Floor, Above Abhinandan Garments, Samad Road, Center Point, Aligarh Locality, Aligarh has been rated - 3.9 and has average price for two people - Rs.200\n\n5. Family Choice Restaurant in dodhpur, civil lines Aligarh, Aligarh Locality, Aligarh has been rated - 3.9 and has average price for two people - Rs.200\n\n6. Deepak's Fast Food in centre point, Aligarh, Aligarh Locality, Aligarh has been rated - 3.9 and has average price for two people - Rs.200\n\n7. Darjeeling Snacks Momo's Point in Centre Point, Zone 6, Aligarh Locality, Aligarh has been rated - 3.9 and has average price for two people - Rs.200\n\n8. Al Bake Fish and Chicken in Shop No. 3-4, City Center, Medical Road, Zone No. 1, Aligarh, UP, Aligarh Locality, Aligarh has been rated - 3.9 and has average price for two people - Rs.200\n\n9. Sher-e-Punjab in Opposite Masjid e Noor, Noor Doodhpur Road, Aligarh Locality, Aligarh has been rated - 3.9 and has average price for two people - Rs.150\n\n10. Pragya Cakes and Bakes in Vishnupuri chauraha, Aligarh, Aligarh Locality, Aligarh has been rated - 3.9 and has average price for two people - Rs.100\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* negative
    - utter_negative
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Auber-Gin in 101, Hub Town, Akriti Sky Bay, Bhulabhai Desai Road, Cumballa Hill, Breach Candy, Mumbai has been rated 4.9\n\n2. La Pino'z Pizza in Shop 4/1, S.V. Road, Opposite Saraf College, Malad West, Mumbai has been rated 4.7\n\n3. Millennials Eatery & Bar in 105, Mumbai Samachar Marg, Apollo Street, Opposite Laxmi Vilas Bank, Fort, Mumbai has been rated 4.6\n\n4. Kyro in 8th Floor, Synergy Building, Kachpada, Malad West, Mumbai has been rated 4.6\n\n5. La Pino'z Pizza in G1, Santoor Residency, Nehru Road, Vile Parle East, Mumbai has been rated 4.5\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Auber-Gin in 101, Hub Town, Akriti Sky Bay, Bhulabhai Desai Road, Cumballa Hill, Breach Candy, Mumbai has been rated - 4.9 and has average price for two people - Rs.1800\n\n2. La Pino'z Pizza in Shop 4/1, S.V. Road, Opposite Saraf College, Malad West, Mumbai has been rated - 4.7 and has average price for two people - Rs.800\n\n3. Millennials Eatery & Bar in 105, Mumbai Samachar Marg, Apollo Street, Opposite Laxmi Vilas Bank, Fort, Mumbai has been rated - 4.6 and has average price for two people - Rs.1500\n\n4. Kyro in 8th Floor, Synergy Building, Kachpada, Malad West, Mumbai has been rated - 4.6 and has average price for two people - Rs.1500\n\n5. La Pino'z Pizza in G1, Santoor Residency, Nehru Road, Vile Parle East, Mumbai has been rated - 4.5 and has average price for two people - Rs.800\n\n6. Lotus Leaf - Eskay Resorts in Eskay Resorts, Eskay House, New Link Road, Borivali West, Mumbai has been rated - 4.5 and has average price for two people - Rs.1500\n\n7. Tipsy Gypsy in Level One, Fun Republic Mall, Off New Link Road, Veera Desai Area, Mumbai has been rated - 4.4 and has average price for two people - Rs.1800\n\n8. Tamasha in Ground Floor, Victoria House, E.B Marg, Lower Parel, Mumbai has been rated - 4.4 and has average price for two people - Rs.2700\n\n9. House Of Thanos in 7/8, Rizvi Mahal Building, Near Bhabha Hospital, Waterfield Road, Linking Road, Bandra West, Mumbai has been rated - 4.4 and has average price for two people - Rs.900\n\n10. Mia Cucina in G3, Transocean House, Lake Boulevard Street, Hiranandani Business Park, Powai, Mumbai has been rated - 4.4 and has average price for two people - Rs.2000\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* negative
    - utter_negative
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - utter_default
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Indian Accent in The Lodhi, Lodhi Road, New Delhi has been rated 4.9\n\n2. Hauz Khas Social in 9-A & 12, Hauz Khas Village, New Delhi has been rated 4.8\n\n3. Ah So Yum in Plot 679, Saraswati Kunj, Sector 53, Golf Course Road, Gurgaon has been rated 4.8\n\n4. Indian Grill Room in 315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon has been rated 4.7\n\n5. Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated 4.7\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Indian Accent in The Lodhi, Lodhi Road, New Delhi has been rated - 4.9 and has average price for two people - Rs.5000\n\n2. Hauz Khas Social in 9-A & 12, Hauz Khas Village, New Delhi has been rated - 4.8 and has average price for two people - Rs.1300\n\n3. Ah So Yum in Plot 679, Saraswati Kunj, Sector 53, Golf Course Road, Gurgaon has been rated - 4.8 and has average price for two people - Rs.1400\n\n4. Indian Grill Room in 315, 3rd Floor, Suncity Business Tower, Golf Course Road, Gurgaon has been rated - 4.7 and has average price for two people - Rs.1800\n\n5. Master Koii's in Shop 19, Flavor Town, Bestech Chambers, Sushant Lok, Gurgaon has been rated - 4.7 and has average price for two people - Rs.1800\n\n6. Gastronomica Kitchen & Bar in M-55, 2nd Floor, M Block Market, Greater Kailash 1 (GK 1), New Delhi has been rated - 4.7 and has average price for two people - Rs.2300\n\n7. Odeon Social in 23, 1st Floor, Odeon Building, Radial 5, D Block, Connaught Place, New Delhi has been rated - 4.7 and has average price for two people - Rs.1300\n\n8. Feel Alive in SCO 53, 2nd Floor, Main Market, Sector 29, Gurgaon has been rated - 4.7 and has average price for two people - Rs.2000\n\n9. C.I.A. Call it Asiian in 13/14/15/16, Narmada Shopping Complex, Opposite Don Bosco School, Alaknanda Road, Greater Kailash 2 (GK 2), New Delhi has been rated - 4.6 and has average price for two people - Rs.700\n\n10. The Clay Oven in D-1, Hotel Park Residency, Green Park, New Delhi has been rated - 4.6 and has average price for two people - Rs.2000\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* negative
    - utter_negative

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_default
* restaurant_search{"cuisine": "american", "location": "pune"}
    - slot{"cuisine": "american"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - slot{"location_found": "found"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Darshan in Amar Business Park, Baner, Pune has been rated 4.9\n\n2. AB's - Absolute Barbecues in Shop 206, 2nd Floor, White Square Building, Opposite Atlanta Complex, Hinjawadi, Pune has been rated 4.9\n\n3. Pop Tate's in Shop T08, 3rd Floor, Phoenix Market City Mall, Viman Nagar, Pune has been rated 4.9\n\n4. Darshan in 759/60, Opposite Indian Bank, Prabhat Road, Deccan Gymkhana, Pune has been rated 4.8\n\n5. Flechazo in 165, 3rd Floor, Vantagio, Near Silver Sports Club, Wakad, Pune has been rated 4.7\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Darshan in Amar Business Park, Baner, Pune has been rated - 4.9 and has average price for two people - Rs.700\n\n2. AB's - Absolute Barbecues in Shop 206, 2nd Floor, White Square Building, Opposite Atlanta Complex, Hinjawadi, Pune has been rated - 4.9 and has average price for two people - Rs.1400\n\n3. Pop Tate's in Shop T08, 3rd Floor, Phoenix Market City Mall, Viman Nagar, Pune has been rated - 4.9 and has average price for two people - Rs.1400\n\n4. Darshan in 759/60, Opposite Indian Bank, Prabhat Road, Deccan Gymkhana, Pune has been rated - 4.8 and has average price for two people - Rs.700\n\n5. Flechazo in 165, 3rd Floor, Vantagio, Near Silver Sports Club, Wakad, Pune has been rated - 4.7 and has average price for two people - Rs.1400\n\n6. The Barkhana in 1st Floor, Commercia Building, Near Hinjawadi Flyover, Wakad, Pune has been rated - 4.7 and has average price for two people - Rs.1700\n\n7. Le Plaisir in Survey 759/125, Rajkamal, Opposite Kelkar Eye Hospital, Prabhat Road, Deccan Gymkhana, Pune has been rated - 4.7 and has average price for two people - Rs.1000\n\n8. The Deccan Bid Capital in 1196/B, Shrushti Chambers, Tukaram Paduka Chowk, Ghole Road, Shivaji Nagar, Pune has been rated - 4.7 and has average price for two people - Rs.1200\n\n9. The Ruby Hilltop - Sunny's World in 217, Pashan-Sus Road, Sus Gaon, Sus, Pune has been rated - 4.7 and has average price for two people - Rs.1300\n\n10. The Ruby Hilltop - Sunny's World in 217, Pashan-Sus Road, Sus Gaon, Sus, Pune has been rated - 4.7 and has average price for two people - Rs.1300\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* negative
    - utter_negative
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "price": "lesser than 300"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "lesser than 300"}
    - utter_ask_location
* negative{"location": "Bareilly"}
    - slot{"location": "Bareilly"}
    - action_check_location
    - slot{"location": "Bareilly"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Bite in civil lines Bombay plaza, Patel chowk, Civil Lines, Bareilly has been rated 4.4\n\n2. Bite [ Prem Nagar ] in HIG-1 BDA Colony, Opposite GRM School, Prem Nagar, Bareilly has been rated 4.3\n\n3. Al Nawab Chicken Biryani in Near Gulab rai inter college, Nainital road, Breilly, Model Town, Bareilly has been rated 4.2\n\n4. Mohan Shudh Sakahari Bhojanalay in Shop 36, Near Chaupla Chauraha, Station Road, Civil Lines, Bareilly has been rated 4.0\n\n5. Shree Laxmi Hindu Hotel in Station Chauraha, dharamshala building, Bareilly, Model Town, Bareilly has been rated 4.0\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Bite in civil lines Bombay plaza, Patel chowk, Civil Lines, Bareilly has been rated - 4.4 and has average price for two people - Rs.200\n\n2. Bite [ Prem Nagar ] in HIG-1 BDA Colony, Opposite GRM School, Prem Nagar, Bareilly has been rated - 4.3 and has average price for two people - Rs.250\n\n3. Al Nawab Chicken Biryani in Near Gulab rai inter college, Nainital road, Breilly, Model Town, Bareilly has been rated - 4.2 and has average price for two people - Rs.250\n\n4. Mohan Shudh Sakahari Bhojanalay in Shop 36, Near Chaupla Chauraha, Station Road, Civil Lines, Bareilly has been rated - 4.0 and has average price for two people - Rs.150\n\n5. Shree Laxmi Hindu Hotel in Station Chauraha, dharamshala building, Bareilly, Model Town, Bareilly has been rated - 4.0 and has average price for two people - Rs.250\n\n6. Bala Ji (Pack  & Go) in A 363/4 Rajendra nagar behind Bake Bihari Mandir, Model Town, Bareilly has been rated - 3.9 and has average price for two people - Rs.250\n\n7. New Laxmi Marwari Hotel in 56 gali arya samaj, Kutubkhana, Civil Lines, Bareilly has been rated - 3.9 and has average price for two people - Rs.250\n\n8. Richers The Chaap Specialist in 242/C Shahdana colony, opposite Indra park, Model town Bareilly, Model Town, Bareilly has been rated - 3.8 and has average price for two people - Rs.250\n\n9. Prabha Restaurant in Opp Diwakar Hospital Mimi Bypass Karamchari Nagar, Izatnagar, Bareilly has been rated - 3.7 and has average price for two people - Rs.200\n\n10. Apni Rasoi (Pack & Tiffin) in Sanjay nagar trimurti raod bareilly has been rated - 3.6 and has average price for two people - Rs.250\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* affirm
    - utter_affirm
* send_email{"email": "hanifkhan.86@gmail.com"}
    - slot{"email": "hanifkhan.86@gmail.com"}
    - action_send_email
    - slot{"email": "hanifkhan.86@gmail.com"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_check_location
    - slot{"location": "bengaluru"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_pricerange
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Byg Brewski Brewing Company in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore has been rated 4.9\n\n2. Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore has been rated 4.9\n\n3. Brahma Brews in 24th Main, 7th Phase, Opposite Brigade Palm Springs, JP Nagar, Bangalore has been rated 4.9\n\n4. Street Storyss in Srinivasan Towers, ESI Hospital Road, Indiranagar, Bangalore has been rated 4.9\n\n5. TBC- Sky Lounge in 36/1, 5th Floor, Berry's Hotel, Kadubeesanahalli, Opposite JP Morgan, Ring Road, Marathahalli, Bangalore has been rated 4.9\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Byg Brewski Brewing Company in 22/123, Byrathi Village, Bidarahalli Hobli, Hennur, Bangalore has been rated - 4.9 and has average price for two people - Rs.1600\n\n2. Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore has been rated - 4.9 and has average price for two people - Rs.1600\n\n3. Brahma Brews in 24th Main, 7th Phase, Opposite Brigade Palm Springs, JP Nagar, Bangalore has been rated - 4.9 and has average price for two people - Rs.1850\n\n4. Street Storyss in Srinivasan Towers, ESI Hospital Road, Indiranagar, Bangalore has been rated - 4.9 and has average price for two people - Rs.1300\n\n5. TBC- Sky Lounge in 36/1, 5th Floor, Berry's Hotel, Kadubeesanahalli, Opposite JP Morgan, Ring Road, Marathahalli, Bangalore has been rated - 4.9 and has average price for two people - Rs.1600\n\n6. Biergarten in 4th B Cross, Koramangala 5th Block, Bangalore has been rated - 4.9 and has average price for two people - Rs.2600\n\n7. TBC Sky Lounge in Astra Hotel, 2795, 27th Main, Sector 1, HSR, Bangalore has been rated - 4.9 and has average price for two people - Rs.1600\n\n8. UDP Urban Deccan Pub in 4032, 100 Feet Road, HAL 2nd Stage, Near Domlur Bridge, Indiranagar, Bangalore has been rated - 4.9 and has average price for two people - Rs.1400\n\n9. House Of Commons in 122/B, Jyothi Nivas Road, Koramangala 5th Block, Bangalore has been rated - 4.9 and has average price for two people - Rs.1300\n\n10. Barbeque Nation in 4005, HAL 2nd Stage, 100 Feet Road, Indiranagar, Bangalore has been rated - 4.9 and has average price for two people - Rs.1600\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* send_email{"email": "hanifkhan.86@gmail.com"}
    - slot{"email": "hanifkhan.86@gmail.com"}
    - action_send_email
    - slot{"email": "hanifkhan.86@gmail.com"}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "amritsar", "price": "between 300 to 700"}
    - slot{"location": "amritsar"}
    - slot{"price": "between 300 to 700"}
    - action_check_location
    - slot{"location": "amritsar"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. La Roma Pizzeria in SCO 6, District Shopping Complex, Ranjit Avenue, Amritsar has been rated 4.9\n\n2. Charming Chicken in Shop 3, Opposite Nari Nikaten, Majithia Road, Near, Basant Nagar, Amritsar has been rated 4.6\n\n3. Kesar Da Dhabha in Near Telephone Exchange, Chowk Passian, Shastri Market, Near Town Hall, Amritsar has been rated 4.5\n\n4. R K Food Plaza in Opposite Amrit Talkies, Inside Hall Gate, Katra Kanhaiyan, Town Hall, Amritsar has been rated 4.4\n\n5. Bade Bhai ka Brothers Dhaba in 1 Town hall, Opposite Partition Museum, Amritsar has been rated 4.4\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. La Roma Pizzeria in SCO 6, District Shopping Complex, Ranjit Avenue, Amritsar has been rated - 4.9 and has average price for two people - Rs.500\n\n2. Charming Chicken in Shop 3, Opposite Nari Nikaten, Majithia Road, Near, Basant Nagar, Amritsar has been rated - 4.6 and has average price for two people - Rs.600\n\n3. Kesar Da Dhabha in Near Telephone Exchange, Chowk Passian, Shastri Market, Near Town Hall, Amritsar has been rated - 4.5 and has average price for two people - Rs.500\n\n4. R K Food Plaza in Opposite Amrit Talkies, Inside Hall Gate, Katra Kanhaiyan, Town Hall, Amritsar has been rated - 4.4 and has average price for two people - Rs.400\n\n5. Bade Bhai ka Brothers Dhaba in 1 Town hall, Opposite Partition Museum, Amritsar has been rated - 4.4 and has average price for two people - Rs.500\n\n6. Beera Chicken House in Opposite Bandari Hospital, Sehaj Avenue, Majitha Road, Near, Basant Nagar, Amritsar has been rated - 4.4 and has average price for two people - Rs.500\n\n7. Life Bakery in 7 East Mohan Nagar, 100 Feet Road Mohan Nagar, Amritsar has been rated - 4.3 and has average price for two people - Rs.500\n\n8. Brothers Dhaba in Lic Building, Khandwala Chheharta, GNDU Area, Amritsar has been rated - 4.3 and has average price for two people - Rs.300\n\n9. McDonald's in Plot no.1615,1616/1768, Gali kashmirian, Near jallianwala bagh, Amritsar-143001,, Town Hall, Amritsar has been rated - 4.3 and has average price for two people - Rs.300\n\n10. Brothers' Amritsari Dhaba in Phawara Chowk, Town Hall, Amritsar has been rated - 4.2 and has average price for two people - Rs.400\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* affirm
    - utter_affirm
* send_email{"email": "hanifkhan.86@gmail.com"}
    - slot{"email": "hanifkhan.86@gmail.com"}
    - action_send_email
    - slot{"email": "hanifkhan.86@gmail.com"}
* goodbye
    - utter_goodbye
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - slot{"location": "Bengaluru"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_pricerange
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"search_results": "Showing you top 5 results in your budget range :\n\n1. Meghana Foods in 52, 1st Floor, 33rd Cross, 4th Block, Jayanagar, Bangalore has been rated 4.5\n\n2. The Hole In The Wall Cafe in 4, 8th Main Road, Koramangala 4th Block, Bangalore has been rated 4.5\n\n3. eat.fit in 96, 29th Main, 23rd Cross, 2nd Stage, BTM, Bangalore has been rated 4.3\n\n4. Meghana Foods in 124, KHB Colony, 1st Cross, Near Jyothi Nivas College, Koramangala 5th Block, Bangalore has been rated 4.3\n\n5. Leon Grill in 18th Cross, Near Reliance Digital, Sector 3, HSR, Bangalore has been rated 4.3\n\n"}
    - slot{"email_results": "Hi,\n\nHere is the list of the restaurants you requested - \n1. Meghana Foods in 52, 1st Floor, 33rd Cross, 4th Block, Jayanagar, Bangalore has been rated - 4.5 and has average price for two people - Rs.600\n\n2. The Hole In The Wall Cafe in 4, 8th Main Road, Koramangala 4th Block, Bangalore has been rated - 4.5 and has average price for two people - Rs.600\n\n3. eat.fit in 96, 29th Main, 23rd Cross, 2nd Stage, BTM, Bangalore has been rated - 4.3 and has average price for two people - Rs.400\n\n4. Meghana Foods in 124, KHB Colony, 1st Cross, Near Jyothi Nivas College, Koramangala 5th Block, Bangalore has been rated - 4.3 and has average price for two people - Rs.600\n\n5. Leon Grill in 18th Cross, Near Reliance Digital, Sector 3, HSR, Bangalore has been rated - 4.3 and has average price for two people - Rs.650\n\n6. eat.fit in 1st Floor, BRS Towers, Kaikondrahalli, Sarjapur Road, Bangalore has been rated - 4.2 and has average price for two people - Rs.400\n\n7. eat.fit in 32/2G, NCPR Industrial Layout, Doddanakundi Industrial Area 2, Seetharampalya, Hoodi, Whitefield, Bangalore has been rated - 4.2 and has average price for two people - Rs.400\n\n8. Meghana Foods Grand in 90/4, Above Sony Centre, Opposite Park Plaza, Outer Ring Road, Marathahalli, Bangalore has been rated - 4.2 and has average price for two people - Rs.600\n\n9. eat.fit in Old 2, New 4, Old Binnamangala Village, Ward 82, Mahadevpura, Indiranagar, Bangalore has been rated - 4.2 and has average price for two people - Rs.400\n\n10. Kota Kachori in 635, 100 Feet Road, Koramangala 6th Block, Bangalore has been rated - 4.2 and has average price for two people - Rs.400\n\nThanks,\nRestaurant Chatbot"}
    - utter_ask_email
* affirm
    - utter_affirm
* send_email{"email": "hanifkhan.86@gmail.com"}
    - slot{"email": "hanifkhan.86@gmail.com"}
    - action_send_email
    - slot{"email": "hanifkhan.86@gmail.com"}
* goodbye
    - utter_goodbye
