module.exports = {
    calculate(formula) {
        try {
            return eval(`(function() { return ${ formula } ;}())`);

        } catch (e) {
            if (e instanceof SyntaxError) {
                return 'Something went wrong!';
            }
        }
    }
}


// ocd