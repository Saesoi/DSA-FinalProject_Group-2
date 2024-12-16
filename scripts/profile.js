// profile.js

// Profile data
const profiles = [
    {
        image: '/images/jahren.jpg',
        name: 'Jahren D. Ricamara',
        course: 'BSCpE 2-2',
        quote: '“Things will work out.”'
    },
    {
        image: '/images/roan.jpg',
        name: 'Jan Roan D. Abad',
        course: 'BSCpE 2-2',
        quote: '“Always there but never good enough to be there.”'
    },
    {
        image: '/images/chelzy.jpg',
        name: 'Chelzy Anne M. Guanlao',
        course: 'BSCpE 2-2',
        quote: '“If it makes you happy, then it is not a waste of time.”'
    },
    {
        image: '/images/maxene.jpg',
        name: 'Maxene Monina P. Carcillar',
        course: 'BSCpE 2-2',
        quote: '“Things take time.”'
    },
    {
        image: '/images/margarette.jpg',
        name: 'Margarette L. Vergara',
        course: 'BSCpE 2-2',
        quote: '“Forge your own way; no map is needed for your journey.”'
    },
    {
        image: '/images/cy.jpg',
        name: 'Cyrane Trisha R. Sevilla',
        course: 'BSCpE 2-2',
        quote: '“if life hurts, @saythename_17 heals.”'
    },
    {
        image: '/images/cabali.jpg',
        name: 'Carl Errol G. Cabali',
        course: 'BSCpE 2-2',
        quote: '“Poetry, beauty, romance, love, these are what we stay alive for.”'
    }

];

// Current profile index
let currentProfileIndex = 0;

// Function to show profile at the current index
function showProfile(index) {
    const profile = profiles[index];

    document.getElementById('profile-image').src = profile.image;
    document.getElementById('profile-name').textContent = profile.name;
    document.getElementById('profile-course').textContent = profile.course;
    document.getElementById('profile-quote').textContent = profile.quote;
}

// Function to show the previous profile
function prevProfile() {
    currentProfileIndex = (currentProfileIndex === 0) ? profiles.length - 1 : currentProfileIndex - 1;
    showProfile(currentProfileIndex);
}

// Function to show the next profile
function nextProfile() {
    currentProfileIndex = (currentProfileIndex === profiles.length - 1) ? 0 : currentProfileIndex + 1;
    showProfile(currentProfileIndex);
}

// Initial profile
showProfile(currentProfileIndex);
