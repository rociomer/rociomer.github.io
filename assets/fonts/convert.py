# convert.py
# First install fontforge: brew install fontforge
# Then, to run: fontforge -script convert.py
import fontforge

font = fontforge.open("fa-brands-400.svg")

# Generate TTF
font.generate("fa-brands-400.ttf")

# Generate EOT (legacy IE)
font.generate("fa-brands-400.eot")

# Generate WOFF (Web Open Font Format)
font.generate("fa-brands-400.woff")

# Generate WOFF2 (more compressed)
font.generate("fa-brands-400.woff2")
