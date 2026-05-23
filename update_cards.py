import glob
from bs4 import BeautifulSoup
import re

files = [
    "digital_marketing.html",
    "sms_services.html",
    "whatsapp_api.html",
    "custom_sw.html",
    "support.html"
]

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all flip card groups
    # We look for divs with class containing [perspective:1000px]
    cards = soup.find_all('div', class_=lambda c: c and '[perspective:1000px]' in c)
    modified = False
    
    for card in cards:
        # 1. Update the main group classes
        classes = card.get('class', [])
        if 'h-[320px]' in classes:
            classes[classes.index('h-[320px]')] = 'h-auto md:h-[320px]'
        else:
            # Maybe it is just a string, bs4 parses classes to list usually
            if 'h-auto' not in classes:
                classes.append('h-auto md:h-[320px]')
                
        if '[perspective:1000px]' in classes:
            classes[classes.index('[perspective:1000px]')] = 'md:[perspective:1000px]'
        
        card['class'] = " ".join(classes)
        
        # Find the inner div that flips
        inner = card.find('div', class_=lambda c: c and 'group-hover:[transform:rotateY(180deg)]' in c)
        if not inner:
            continue
            
        inner_classes = inner.get('class', [])
        if '[transform-style:preserve-3d]' in inner_classes:
            inner_classes[inner_classes.index('[transform-style:preserve-3d]')] = 'md:[transform-style:preserve-3d]'
        if 'group-hover:[transform:rotateY(180deg)]' in inner_classes:
            inner_classes[inner_classes.index('group-hover:[transform:rotateY(180deg)]')] = 'md:group-hover:[transform:rotateY(180deg)]'
        
        inner['class'] = " ".join(inner_classes)
        
        # Front and Back sides
        sides = inner.find_all('div', recursive=False)
        if len(sides) < 2:
            continue
            
        front = sides[0]
        back = sides[1]
        
        # Get background color from back side
        back_classes = back.get('class', [])
        bg_color_class = None
        for c in back_classes:
            if c.startswith('bg-') and c != 'bg-white':
                bg_color_class = c
                break
        
        if not bg_color_class:
            continue
            
        # Modify Front
        front_classes = front.get('class', [])
        if 'absolute' in front_classes:
            front_classes[front_classes.index('absolute')] = 'relative md:absolute'
        if '[backface-visibility:hidden]' in front_classes:
            front_classes[front_classes.index('[backface-visibility:hidden]')] = 'md:[backface-visibility:hidden]'
        
        if 'bg-white' in front_classes:
            front_classes[front_classes.index('bg-white')] = f'{bg_color_class} md:bg-white'
            
        # Fix border
        if 'border' in front_classes:
            # We want border border-transparent md:border-slate-100
            # Wait, usually it is border border-slate-100
            if 'border-slate-100' in front_classes:
                front_classes[front_classes.index('border-slate-100')] = 'border-transparent md:border-slate-100'
        
        # Fix shadow
        if 'shadow-sm' in front_classes:
            front_classes[front_classes.index('shadow-sm')] = 'shadow-lg md:shadow-sm'
            
        front['class'] = " ".join(front_classes)
        
        # Modify Front text and icon
        icon_container = front.find('div', class_=lambda c: c and 'rounded-2xl' in c)
        if icon_container:
            ic_classes = icon_container.get('class', [])
            # bg-color-100 -> bg-white/20 md:bg-color-100
            # text-color-600 -> text-white md:text-color-600
            for i, c in enumerate(ic_classes):
                if c.startswith('bg-') and not 'bg-white' in c:
                    ic_classes[i] = f"bg-white/20 md:{c}"
                elif c.startswith('text-'):
                    ic_classes[i] = f"text-white md:{c}"
            icon_container['class'] = " ".join(ic_classes)
            
        h3_front = front.find('h3')
        if h3_front:
            h3_classes = h3_front.get('class', [])
            if 'mb-4' in h3_classes:
                h3_classes[h3_classes.index('mb-4')] = 'md:mb-4'
            if 'text-slate-900' in h3_classes:
                h3_classes[h3_classes.index('text-slate-900')] = 'text-white md:text-slate-900'
            h3_front['class'] = " ".join(h3_classes)
            
        # Add description to front
        p_back = back.find('p')
        if p_back and not front.find('p', class_=lambda c: c and 'block md:hidden' in c):
            p_desc = soup.new_tag('p')
            # Extract color-50 from p_back to use as text color on front
            p_back_classes = p_back.get('class', [])
            text_color_class = 'text-slate-50' # fallback
            for c in p_back_classes:
                if c.startswith('text-'):
                    text_color_class = c
                    break
            
            p_desc['class'] = f"{text_color_class} leading-relaxed block md:hidden mt-4"
            p_desc.string = p_back.string.strip() if p_back.string else p_back.get_text(strip=True)
            front.append(p_desc)
            
        # Modify Back
        back_classes_new = []
        for c in back_classes:
            if c == 'absolute':
                back_classes_new.append('hidden md:flex absolute')
            elif c == 'flex':
                back_classes_new.append('flex-col')
            elif c == 'flex-col':
                pass # Already added
            else:
                back_classes_new.append(c)
        back['class'] = " ".join(back_classes_new)
        
        modified = True
        
    if modified:
        # Write back unescaped formatting (bs4 can mess up formatting a bit, but we'll try to keep it minimal)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated {filename}")
    else:
        print(f"No changes in {filename}")
