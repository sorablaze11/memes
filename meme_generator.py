from PIL import Image, ImageDraw, ImageFont
import textwrap

def meme_generator(image_path, top_text, bottom_text='', font_path='impact/impact.ttf', font_size=9):
    
    
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    image_width, image_height = img.size
    
    
    font = ImageFont.truetype(font = font_path, size = int(image_height*font_size)//100)
    
    
    top_text = top_text.upper()
    bottom_text = bottom_text.upper()

    
    char_width, char_height = font.getsize('A')
    chars_per_line = image_width // char_width
    top_lines = textwrap.wrap(top_text, width = chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width = chars_per_line)
    
    
    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x,y), line, fill='white', font=font)
        y += line_height

   
    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x,y), line, fill='white', font=font)
        y += line_height

    
    img.save('meme-' + img.filename.split('/')[-1])

if __name__ == '__main__':
    top_text = "Input the top line here"
    bottom_text = "Input the bottom line here"
meme_generator('input_image.jpg', top_text, bottom_text)