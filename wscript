# arjun

# set folder names
out='results'
TESTDIR='tests'
STANDARDS='tests/reference'

# set meta-information
script='guru'
APPNAME='nlci-' + script
VERSION='0.100'
TTF_VERSION='0.100'
COPYRIGHT='Copyright (c) 2009-2015, NLCI (http://www.nlci.in/fonts/)'

DESC_SHORT='Gurmukhi Unicode font with OT support'
DESC_LONG='''
Pan Gurmukhi font designed to support all the languages using the Gurmukhi script.
'''
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script

# set test parameters
TESTSTRING=u'\u0a15'

# set fonts to build
faces = ('Arjun',)
facesLegacy = ('ARJU',)
styles = ('-R', '-B', '-I')
stylesName = ('Regular', 'Bold', 'Italic')
stylesLegacy = ('', 'BD', 'I')

# set build parameters
fontbase = 'source/'

for f, fLegacy in zip(faces, facesLegacy):
    for (s, sn, sLegacy) in zip(styles, stylesName, stylesLegacy):
        font(target = process(script.title() + f + s + '.ttf',
                cmd('psfix ${DEP} ${TGT}'),
                name(script.upper() + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = legacy(f + s + '.ttf',
                            source = fontbase + 'archive/' + fLegacy + sLegacy + '.ttf',
                            xml = fontbase + 'arjun_unicode.xml',
                            noap = ''),
            opentype = internal(),
            #graphite = gdl(fontbase + f + s + '.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2 -l first',
            #    params = '-d -v2'
            #    ),
            #classes = fontbase + 'arjun_classes.xml',
            ap = f + s + '.xml',
            version = TTF_VERSION,
            copyright = COPYRIGHT,
            license = ofl('Arjun', 'NLCI'),
            woff = woff(),
            script = 'guru',
            fret = fret(params = '-r')
        )
