function scrollToSection(event) {
    event.preventDefault();
    const targetId = event.currentTarget.getAttribute("href");
    const targetElement = document.querySelector(targetId);
    
    targetElement.scrollIntoView({
      behavior: "smooth",
      block: "start"
    });
  }
  
  document.querySelectorAll("#navbar a").forEach((navLink) => {
    navLink.addEventListener("click", scrollToSection);
  });
  