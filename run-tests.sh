# Run tests
if [ -d "tests-env" ]; then
        echo tests-exists
else
        virtualenv tests-env
        tests-env/bin/pip install nose
fi
# clear old tests
rm -f *.xml

tests-env/bin/nosetests --with-xunit
