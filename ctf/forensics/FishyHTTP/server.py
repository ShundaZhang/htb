from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import urllib.parse

import base64

def extract_and_decode(words):
    first_letters = ''.join(word[0] for word in words if word)

    #print("Extracted first letters:", first_letters)

    try:
        decoded_bytes = base64.b64decode(first_letters)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except Exception as e:
        return f"Error decoding Base64 string: {e}"


# HTML content for different pages
pages = [
    '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Web Server</title>
</head>
<body><button>leaf tree glasses uniform guitar tiger umbrella book</button>
<button>panda universe quartz laptop</button>
<ol><li>rabbit jewel avocado sun plane</li></ol>
<div>house ball elephant trumpet fence mango fire hedgehog</div>
<ol><li>jar garden</li></ol>
<blockquote>mango yucca yurt bird lion</blockquote>
<ol><li>ball question apple necklace penguin zone xanthan quadrilateral</li></ol>
<h1>ice universe car tooth castle</h1>
<ol><li>notebook popcorn flag helicopter ant mailbox</li></ol>
<b>dinosaur door octopus</b>
<ol><li>mouse pencil grape quill pear utensil quiver</li></ol>
<span>utensil elephant grape cookie apple heart yucca knight anchor</span>
</body>
</html>
    ''',
    '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Web Server</title>
</head>
<body><button>kangaroo kettle horn</button>
<a href="#">watermelon egg snake nose instrument urn xerophyte yogurt</a>
<button>gift underground pencil eraser pizza yolk mask koala ladder</button>
<span>knight fire leaf jewel popcorn tambourine necklace xylulose</span>
<button>whale underground hedgehog wing fruit bottle honey pencil</button>
<a href="#">urn windmill snake tambourine</a>
<button>umbrella zebra</button>
<img src=quartz ocean>
<ol><li>king tooth house key necklace dolphin xerophyte escalator</li></ol>
<ul><li>ring fruit camera jump cookie table basket nail universe</li></ul>
<ol><li>ink sun ladybug beach hat urn kitchen</li></ol>
<b>clown whale kettle lion jungle king</b>
<ol><li>diamond garden penguin quill quail zigzag apple</li></ol>
<span>invitation ocean uniform volcano</span>
<ol><li>vacuum drum bottle flower</li></ol>
<i>fire turtle squirrel</i>
<ol><li>kettle house horn panda hedgehog xerosis tree astronaut</li></ol>
<ol><li>instrument bird</li></ol>
<ol><li>anchor yew jacket invitation quilt</li></ol>
<blockquote>log easel</blockquote>
</body>
</html>
    ''',
    '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Web Server</title>
</head>
<body><ol><li>eagle horn feather zero hat acrobat</li></ol>
<img src=easel duck>
<ol><li>zigzag ink jump</li></ol>
<span>onion ninja basket watermelon wheel</span>
<button>wagon acrobat keyboard wheel quilt</button>
<p>jacket zen pyramid yellow pizza computer album penguin garden</p>
<p>tiger honey bear heart</p>
<cite>juice game pencil door helicopter quarterback wand</cite>
<p>zoo bird bottle pear ant wand</p>
<ol><li>rocket wallet owl xylitol garden gem guitar</li></ol>
<p>cloud notebook dragon</p>
<ol><li>yak ocean jewel acrobat penguin rainbow snake insect ball</li></ol>
<p>uniform table kite dog zap jacket computer anchor xerophyte</p>
<cite>pencil pumpkin candle xanthan leaf instrument vine kite feather key</cite>
<ol><li>spider</li></ol>
<a href="#">bear vase bicycle</a>
<ol><li>instrument turtle quill raccoon garden xylophone zipper pear owl</li></ol>
<img src=windmill feather mouse vegetable>
<p>nail orange volcano magnet apple vine envelope unicorn fruit cookie</p>
<cite>zero juice</cite>
<ul><li>bear utensil zone egg beach avocado</li></ul>
<nav>universe jar</nav>
<ul><li>clown yurt kettle mushroom fire monkey earth nail</li></ul>
<ul><li>knight rocket beach cat rug</li></ul>
<button>xenon clown jungle necklace microphone lemon banana kite mountain question</button>
<a href="#">nail net vine nest flag</a>
<ol><li>rug monkey</li></ol>
<ul><li>key star</li></ul>
<button>xerosis raccoon magnet ant dragon volcano</button>
<p>sandwich xerosis candle popcorn sun easel cookie plane question unicorn</p>
<button>zero xerosis ice-cream fish acrobat</button>
<a href="#">watermelon goat bicycle jump butterfly basket owl</a>
<ul><li>ring elf eraser zipper popcorn plane xylulose</li></ul>
<nav>king urn utensil tooth umbrella wheel quiver squirrel moon</nav>
<button>kite rabbit jack-o-lantern microphone penguin kettle nest otter</button>
<cite>yawn mango ocean spider engine snowman quiver</cite>
<ol><li>key candle magnet</li></ol>
<h1>dragon dinosaur</h1>
<ol><li>vacuum ring pencil tree hamburger utensil insect iron unicycle</li></ol>
<textarea>cake rocket egg goat envelope drum unicycle</textarea>
<ol><li>kayak video pineapple quadrilateral</li></ol>
<a href="#">honey wagon clown</a>
<button>nose banana instrument tiger unicycle trumpet train rocket album</button>
<span>moon</span>
<ol><li>wheel upholsterer</li></ol>
<p>jet whale iguana mask</p>
<ol><li>quarterback volcano lion</li></ol>
<ul><li>unicorn net acrobat unicycle bird panda worm ship jigsaw yodel</li></ul>
<button>yolk arrow mailbox ladder iguana quiver xebec kitchen</button>
<p>yawn candle key yodel gift butterfly</p>
<ol><li>windmill utensil quartz rose</li></ol>
<p>yurt vegetable nest</p>
<ol><li>elephant lemon jungle dog cloud arrow cake net onion mango</li></ol>
<blockquote>igloo eraser watch ladder rocket unicycle hedgehog xmas</blockquote>
<button>vine</button>
<img src=bird drum mouse otter cake acrobat goat car>
<ul><li>vine basket</li></ul>
<nav>van mailbox nut monkey pencil alarm</nav>
<img src=zombie desk elephant hammer>
<img src=oven rocket necklace umbrella computer bicycle escalator butterfly>
<ol><li>video pencil nail quartz spider ball quadrilateral</li></ol>
<blockquote>hamburger wallet tooth king yodel candle</blockquote>
<ol><li>volcano basket igloo instrument heart juice jump lemon onion</li></ol>
<a href="#">zero hat lock airplane laptop jigsaw windmill tooth banana doll</a>
<button>guitar whale x-ray candle</button>
<ul><li>basket astronaut oven sandwich</li></ul>
<ol><li>escalator easel vase quilt x-ray jet dinosaur otter nest</li></ol>
<b>jacket goat otter</b>
<ol><li>vulture invitation mountain tooth flashlight nest camera vegetable xylitol train</li></ol>
<ul><li>mouse mask cake violin volcano castle newspaper jacket</li></ul>
<ol><li>ruler lemon king banana necklace island gift spoon leaf sock</li></ol>
<i>mouse hedgehog hamburger sun beach zigzag</i>
<button>lemon leaf umbrella yucca tiger ninja</button>
<img src=wing wallet question kangaroo vine iron snake yodel knight jungle>
<button>panda</button>
<a href="#">mask noodles elf jungle spoon clown unicycle</a>
<ul><li>igloo jellyfish basket ship</li></ul>
<nav>laptop invitation cloud zap underground pyramid ninja violin fence</nav>
<p>glasses yodel umbrella</p>
<cite>lion tomato bird yellow octopus hammer lock</cite>
<p>nest</p>
<ol><li>garden windmill ninja violin elf</li></ol>
<p>unicorn tambourine fence question acrobat</p>
<ol><li>jack-o-lantern hat pyramid moon</li></ol>
<p>gift yawn horse pear grape kangaroo</p>
<cite>rocket ball ocean key turtle vegetable vest mango banana dragon</cite>
<button>owl kitchen quail star oven yawn unicorn</button>
<img src=video zebra xebec mask turtle kayak>
<button>bottle igloo trumpet leaf garden mountain video raccoon ladder engine</button>
<span>turtle diamond tooth ship yellow xmas computer monkey vacuum dog</span>
<button>ghost net invitation pear vine glasses envelope ring panda</button>
<cite>computer car grape lion yawn flag ghost table jack-o-lantern castle</cite>
<ol><li>jump horse arrow leaf mailbox</li></ol>
<ul><li>octopus</li></ul>
<p>igloo utensil quartz</p>
<cite>vine frog hamburger volcano apple zebra universe</cite>
<img src=frog flag iguana spoon lion panda kettle fence vacuum watermelon>
<div>quiver jungle ghost vest ant leaf gift tree</div>
<ul><li>cookie book zero noodles tiger helicopter xylulose quartz pencil</li></ul>
<img src=pumpkin yew dog ice-cream banana>
<img src=knight zigzag avocado quail yellow van otter rose yew universe>
<p>heart jar hamburger cloud</p>
<button>fence star gem yogurt banana</button>
<textarea>zipper vine honey zero newspaper uniform jack-o-lantern pizza trumpet</textarea>
<ul><li>quarterback hedgehog</li></ul>
<img src=horse watermelon pear van yurt tiger>
<ol><li>wagon hat lighthouse dolphin yak otter ukulele ladder</li></ol>
<div>dinosaur plane oyster zipper elf wheel garden owl desk ukulele</div>
<a href="#">cat vacuum</a>
<img src=candle banana hammer unicorn yak xmas keyboard telescope zigzag>
<button>radio urn</button>
<img src=ghost fruit quartz flashlight yodel jellyfish worm ring>
<button>fish instrument</button>
<a href="#">grape orange noodles lion yurt garden</a>
<ul><li>pumpkin hammer oyster bird honey</li></ul>
<blockquote>tree wand koala vase ball quartz</blockquote>
<ol><li>ukulele horse jungle octopus juice plane fruit bird</li></ol>
<img src=pear sock vegetable olive iron necklace flag yogurt quail radio>
<a href="#">house spoon quadrilateral avocado zombie</a>
<cite>xerosis jump pencil</cite>
<a href="#">computer drum ship watermelon quill helicopter rainbow moon</a>
<button>log noodles wand xerosis yogurt</button>
<ol><li>train camera quiver rainbow lock cake quilt dog</li></ol>
<i>nose</i>
<a href="#">rainbow knight</a>
<a href="#">keyboard xylitol zoo butterfly astronaut door beach nest x-ray</a>
<a href="#">table kangaroo snake worm
 wing flag</a>
<button>avocado wing moon watch invitation mango</button>
<ul><li>ant rainbow pineapple elephant ship yew clown ladder jump popcorn</li></ul>
<blockquote>wand iron video unicorn nut key yellow</blockquote>
</body>
</html>
    ''',
    '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Web Server</title>
</head>
<body><ol><li>xanthan door ice-cream tooth octopus zoo</li></ol>
<img src=drum wagon bird juice computer butterfly>
<ol><li>door rose dragon ghost tiger jellyfish quartz lion</li></ol>
<span>quadrilateral egg gift zebra sun utensil wing</span>
<button>cake quadrilateral computer sandwich vest</button>
<p>rainbow</p>
<p>kangaroo sandwich game microphone magnet xanthan bottle mountain mushroom</p>
<cite>arrow nut zombie fish ball yogurt flower</cite>
<p>microphone moon octopus oyster wand globe owl van spoon</p>
<ol><li>egg vine raccoon bird island x-ray</li></ol>
<p>lock</p>
<ol><li>escalator ladybug zebra</li></ol>
<p>pizza camera grape diamond hedgehog unicycle hat yurt</p>
<cite>xylulose watch desk robot album flower kite volcano zelda unicorn</cite>
<ol><li>tomato</li></ol>
<a href="#">raccoon</a>
<ol><li>trumpet telescope invitation castle net rose</li></ol>
<img src=pizza sun necklace jungle>
<p>oyster</p>
<cite>ice-cream flower tomato</cite>
<ul><li>watch</li></ul>
<nav>mask flashlight windmill star</nav>
<ul><li>cloud lamp olive easel key vacuum horn newspaper</li></ul>
<ul><li>oyster xylitol arrow ring</li></ul>
<button>sun helicopter mailbox newspaper mouse</button>
<a href="#">fire</a>
<ol><li>umbrella</li></ol>
<ul><li>jack-o-lantern quill mushroom mountain pizza clown ant island castle drum</li></ul>
<button>drum xerophyte utensil owl key</button>
<p>plane moon apple tambourine sock pyramid popcorn avocado quill net</p>
<button>unicorn horn volcano squirrel cloud</button>
<a href="#">tree gift flashlight</a>
<ul><li>jungle astronaut rainbow doll spider quarterback windmill ladder robot</li></ul>
<nav>drum tree orange globe zone train radio penguin ice-cream tomato</nav>
<button>acrobat king basket astronaut horse feather newspaper</button>
<cite>windmill video</cite>
<ol><li>rug mouse</li></ol>
<h1>nose owl hedgehog quill</h1>
<ol><li>rainbow horse flower</li></ol>
<textarea>airplane feather fish rocket dinosaur invitation duck</textarea>
<ol><li>engine jar volcano yurt</li></ol>
<a href="#">utensil wheel zebra radio pyramid pencil avocado xanthan vine</a>
<button>ukulele keyboard rug watch olive</button>
<span>hamburger mountain drum doll tree alarm zone xerosis wand</span>
<ol><li>banana monkey fence vegetable vine cookie earth net gift bottle</li></ol>
<p>desk umbrella beach zebra jump duck island jewel</p>
<ol><li>arrow tree spider cookie</li></ol>
<ul><li>zebra tiger frog upholsterer elephant guitar oven album fruit airplane</li></ul>
<button>ant</button>
<p>dragon quill jewel</p>
<ol><li>dragon</li></ol>
<p>ocean zone lighthouse</p>
<ol><li>microphone uniform vest door wand igloo urn</li></ol>
<blockquote>book acrobat</blockquote>
<button>worm desk hamburger notebook sandwich tomato mailbox pineapple</button>
<img src=key rainbow quill>
<p>juice iguana</p>
<cite>zipper tomato ghost star lamp xerophyte noodles xylophone</cite>
<p>earth ladder laptop spider owl net</p>
<ol><li>worm heart orange jungle ornament quarterback video spider</li></ol>
<p>honey knight kangaroo ghost</p>
<ol><li>nose</li></ol>
<p>worm house orange iron</p>
<cite>ornament iguana</cite>
<ol><li>ghost tomato</li></ol>
<ul><li>cake otter zipper noodles rabbit flag pineapple</li></ul>
<ol><li>vase radio yogurt frog pyramid unicycle unicorn van spoon</li></ol>
<a href="#">igloo zipper zoo anchor nose quadrilateral ice-cream violin utensil xenon</a>
<ol><li>zigzag snake horn bicycle</li></ol>
<div>net</div>
<ol><li>vest rose zap mango kayak yawn heart car spoon watermelon</li></ol>
<blockquote>zelda vegetable snake radio oyster grape laptop anchor apple</blockquote>
<p>king</p>
<cite>ruler instrument yew telescope anchor net</cite>
<p>camera</p>
<button>jacket instrument mouse helicopter tiger kangaroo hamburger yawn grape gift</button>
<button>telescope xmas jigsaw</button>
<span>plane knight xerosis rose kayak wagon airplane</span>
<ol><li>leaf jump elephant star underground tree jack-o-lantern butterfly train</li></ol>
<blockquote>xerophyte</blockquote>
<button>watermelon olive</button>
<ul><li>ink penguin star notebook goat rabbit pear basket net</li></ul>
<p>xylulose quill flag ocean volcano newspaper gift unicycle</p>
<cite>jungle yew newspaper pumpkin</cite>
<ol><li>tambourine ship diamond zap lock mushroom cookie vacuum quilt</li></ol>
<h1>keyboard nut log zebra</h1>
<button>star zigzag</button>
<p>sandwich quarterback spider watch</p>
<ol><li>rocket universe camera door heart queue quilt mushroom wand</li></ol>
<ul><li>instrument bottle nest queen sun</li></ul>
<p>king ornament microphone moon lock</p>
<cite>jungle gem hamburger snowman ukulele kettle candle feather vest</cite>
<ol><li>instrument log butterfly jacket heart unicycle kangaroo</li></ol>
<div>kite basket wheel</div>
<ol><li>ball zombie basket</li></ol>
<h1>lion jungle diamond xylulose van ornament panda popcorn</h1>
<ol><li>album</li></ol>
<a href="#">uniform</a>
<ol><li>star whale goat avocado sandwich duck windmill laptop nail pear</li></ol>
<textarea>ant ruler arrow alarm ukulele xmas noodles knight flashlight</textarea>
<ol><li>jacket xmas quill</li></ol>
<ul><li>house egg igloo volcano ocean kangaroo xerophyte train yawn</li></ul>
<ol><li>zigzag ant gift telescope fish notebook</li></ol>
<img src=mountain gem star rose yak xerosis nut>
<p>quadrilateral zelda moon</p>
<button>pineapple telescope yodel penguin magnet unicycle ring</button>
<p>astronaut wing necklace tomato owl net</p>
<cite>basket pineapple elephant telescope raccoon zen</cite>
<a href="#">x-ray</a>
<i>pizza jar volcano doll</i>
<p>newspaper car guitar universe popcorn fire bird ship</p>
<cite>x-ray jacket vulture zap fruit xanthan fence easel hammer</cite>
<ol><li>lion</li></ol>
<i>rocket yolk sock panda pyramid acrobat</i>
<ol><li>iguana robot rose eagle glasses</li></ol>
<blockquote>car fruit dolphin</blockquote>
<button>grape dolphin</button>
<img src=ball tree engine oven radio king ice-cream pear>
<ol><li>newspaper hamburger fire fence</li></ol>
<ul><li>easel mushroom yolk</li></ul>
<button>lemon arrow</button>
<a href="#">ruler avocado lock nose video popcorn otter queen ball windmill</a>
<p>feather desk book yawn ink arrow juice ant king squirrel</p>
<i>insect feather helicopter oyster star ant desk flag mask gift</i>
<button>zap vegetable upholsterer x-ray</button>
<img src=lion dragon xerophyte gem wing house>
<button>sandwich</button>
<div>rose trumpet clown robot quill banana panda</div>
<button>yolk spider bear raccoon hammer</button>
<img src=van zoo jump wagon oyster>
</body>
</html>
    '''
]

# Track the current page index
current_page_index = 0

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global current_page_index
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Write the HTML content
        self.wfile.write(pages[current_page_index].encode('utf-8'))
        # Update the index for the next request
        current_page_index = (current_page_index + 1) % len(pages)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        parsed_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

        name = parsed_data.get('Name', [''])[0]
        feedback = parsed_data.get('feedback', [''])[0]
        decoded_string = extract_and_decode(feedback.split())
        print(decoded_string)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        response = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Feedback Received</title>
        </head>
        <body>
        <p>Name: {name}</p>
        <p>feedback: {feedback}</p>
        </body>
        </html>
        """
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()

