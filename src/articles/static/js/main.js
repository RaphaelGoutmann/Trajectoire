// responsive menu

const toggleNav = document.querySelector('#toggle-nav')
const nav = document.querySelector('.nav')

const main = document.querySelector('main')

toggleNav.addEventListener('click', (e) =>
{
    document.body.classList.toggle('active')
})

main.addEventListener('click', (e) =>
{
    document.body.classList.remove('active')
})

// search

const searchBtn = document.querySelector('.search')
const searchCloseBtn = document.querySelector('.search-close')

const searchWrapper = document.querySelector('.search-wrapper')

searchBtn.addEventListener('click', (e) =>
{
    searchBtn.classList.add('is-hidden')
    searchCloseBtn.classList.remove('is-hidden')
    searchWrapper.classList.remove('is-hidden')

    searchWrapper.querySelector('form input').focus()
})

searchCloseBtn.addEventListener('click', (e) =>
{
    searchBtn.classList.remove('is-hidden')
    searchCloseBtn.classList.add('is-hidden')
    searchWrapper.classList.add('is-hidden')
})

// dropdown

const dropdowns = document.querySelectorAll('.dropdown')

dropdowns.forEach(dropdown =>
{
    dropdown.addEventListener('click', (e) =>
    {
        dropdown.classList.toggle('active')
    })
})

// data-hide

const hide = document.querySelectorAll('[data-hide]')

hide.forEach(hideElement =>
{
    hideElement.addEventListener('click', (e) =>
    {
        e.preventDefault()
        
        const selector = hideElement.dataset.hide
        const target = document.querySelector(selector)

        if(target)
        {
            target.classList.add('is-hidden')
        }
    })    
})

// data-show

const show = document.querySelectorAll('[data-show]')

show.forEach(showElement =>
{
    showElement.addEventListener('click', (e) =>
    {
        e.preventDefault()
        
        const selector = showElement.dataset.show
        const target = document.querySelector(selector)

        if(target)
        {
            target.classList.remove('is-hidden')
        }
    })    
})

// data-toggle

const toggle = document.querySelectorAll('[data-toggle]')

toggle.forEach(toggleElement =>
{
    toggleElement.addEventListener('click', (e) =>
    {
        e.preventDefault()
        
        const selector = toggleElement.dataset.toggle
        const target = document.querySelector(selector)

        if(target)
        {
            target.classList.toggle('is-hidden')
        }
    })    
})