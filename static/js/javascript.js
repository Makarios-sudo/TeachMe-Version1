

    // Get searchform and page links

    let searchForm = document.getElementById('searchForm')
    let pageLinks = document.getElementsByClassName('btn-link')

    // ensure searchform exist

    if(searchForm){
        for(let i=0; pageLinks.length > i; i++ ){
            pageLinks[i].addEventListener('click', function(e){
                e.preventDefault()
                
                //get data attribute

                let page = this.dataset.page
                

                //add hidden search input to form

                searchForm.innerHTML += `<input value=${page} name='page' hidden/> `

                // submit form
                searchForm.submit()                
                
            })
        }
    }


