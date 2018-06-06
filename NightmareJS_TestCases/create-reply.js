const Nightmare = require('nightmare')

Nightmare()
	.goto('https://github.com/settings/replies')
	
	// Login to GIt
	.type('#login_field', 'residetest')
    .type('#password', 'QWErty654321')
    .click('input[value="Sign in"]')
    .wait(1000)
    
    // Creating test reply
    .type('#saved-reply-title-field', 'Reside test reply')

    // Changing style of header
    .click('button[aria-label = "Add header text"]')
    .click('button[class="dropdown-item dropdown-header3"]')
    
    // Adding text to reply
    .type('#comment_body_1', 'This is a test comment for positive test case of replies function in GIT')
    
    // Add saved reply
    .click('button[class="btn btn-primary"]')
    
    // Verifying that reply is actually present
    .wait('.listgroup') // this selector only appears when saved reply
    .end()
    .then(console.log)
    .catch(error => {
    	console.error('Adding of reply is failed:', error)
    })
