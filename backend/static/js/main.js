document.addEventListener("DOMContentLoaded",()=>{

    console.log("LungScan Ready");

    document.querySelectorAll(".dashboard-card")

    .forEach(card=>{

        card.addEventListener("mouseenter",()=>{

            card.style.transform="translateY(-6px)";

        });

        card.addEventListener("mouseleave",()=>{

            card.style.transform="translateY(0)";

        });

    });

});