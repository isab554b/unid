// ##############################
// PROFILE.HTML

document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".menu_button");

  // Add styling to the first menu button
  if (buttons.length > 0) {
    buttons[0].classList.add("secondary_button_selected");
  }

  // Function to remove stylingn
  function removeSelectedClass() {
    buttons.forEach((button) => {
      button.classList.remove("secondary_button_selected");
    });
  }

  // Add event listener to each button
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      // Remove 'selected' styling from all buttons (only the clicked button is styled)
      removeSelectedClass();
      // Apply 'selected' styling to clicked menu button
      button.classList.add("secondary_button_selected");

      // Load the content and update URL based on the template of the clicked button
      const templateName = button.getAttribute("data-template");
      if (templateName) {
        loadTemplate(templateName);
        updateURL(templateName);
      }
    });
  });

  // Update URL with template name
  function updateURL(templateName) {
    window.location.hash = `/${templateName}`;
  }

  // Load templates dynamically
  function loadTemplate(templateName) {
    fetch(`/profile/${templateName}`)
      .then((response) => response.text())
      .then((html) => {
        console.log(`Template loaded successfully`);
        document.getElementById("profile_content").innerHTML = html;
      })
      .catch((error) => console.error("Error loading template:", error));
  }

  // Open pop up button
  const openButton = document.getElementById("open_logout_pop_up");
  if (openButton) {
    openButton.addEventListener("click", function () {
      const popup = document.getElementById("logout_popup");
      if (popup) popup.classList.remove("object_hidden");
    });
  }

  // Close pop up button
  const closeButton = document.getElementById("close_logout_pop_up");
  if (closeButton) {
    closeButton.addEventListener("click", function () {
      const popup = document.getElementById("logout_popup");
      if (popup) popup.classList.add("object_hidden");
    });
  }
});

// ##############################
// SIGNUP.HTML

async function signUp() {
  // Retrieve user input values from the signup form
  const first_name = document.querySelector("input[name='first_name']").value;
  const last_name = document.querySelector("input[name='last_name']").value;
  const email = document.querySelector("input[name='email']").value;
  const phone = document.querySelector("input[name='phone']").value;
  const username = document.querySelector("input[name='username']").value;
  const password = document.querySelector("input[name='password']").value;
  const website_name = document.querySelector(
    "input[name='website_name']"
  ).value;
  const website_url = document.querySelector("input[name='website_url']").value;

  // Check if the terms checkbox is checked
  const termsAccepted = document.querySelector(
    "input[name='terms_accepted']"
  ).checked;

  console.log("this is the username", username);
  console.log("Terms accepted value:", termsAccepted);

  // Create a FormData object to store form data and append user input values to the FormData object
  const formData = new FormData();
  formData.append("first_name", first_name);
  formData.append("last_name", last_name);
  formData.append("email", email);
  formData.append("phone", phone);
  formData.append("username", username);
  formData.append("password", password);
  formData.append("website_name", website_name);
  formData.append("website_url", website_url);
  formData.append("terms_accepted", termsAccepted); // Append terms_accepted

  // Log form data values for debugging
  for (const [key, value] of formData.entries()) {
    console.log(key, value);
  }

  try {
    // Send a POST request to the server with the form data
    const response = await fetch("/signup", {
      method: "POST",
      body: formData,
    });

    // Parse the response JSON data
    const data = await response.json();

    // If the response contains an error, display it on the signup form
    if (data.error) {
      document.getElementById("error_message").innerText = data.error;
      document.getElementById("form_input_error_message").style.display =
        "flex";
    } else {
      // If signup is successful, log a success message and redirect to the homepage
      console.log("Signup successful");
      window.location.href = "/";
    }
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("error_message").innerText =
      "An unexpected error occurred.";
    document.getElementById("form_input_error_message").style.display = "flex";
  }
}

// ##############################
// LOGIN.HTML

// Handles form submission and processing for user login.
async function login(event) {
  event.preventDefault();
  // Retrieves the username and password entered by the user
  const username = document.querySelector("input[name='username']").value;
  const password = document.querySelector("input[name='password']").value;

  // Creates a FormData object and appends the username and password to it
  const formData = new FormData();
  formData.append("username", username);
  formData.append("password", password);

  try {
    // Sends a POST request to the server with the login credentials
    const response = await fetch("/login", {
      method: "POST",
      body: formData,
    });

    // Check if the response is JSON
    const contentType = response.headers.get("content-type");
    if (contentType && contentType.indexOf("application/json") !== -1) {
      const data = await response.json();

      if (data.error) {
        // If the response contains an error, display it on the login form
        document.getElementById("error_message").innerText = data.error;
        document.getElementById("form_input_error_message").style.display =
          "flex";
      } else {
        // If login is successful, log a success message and redirect to the homepage
        console.log("Login successful");
        window.location.href = "/profile";
      }
    } else {
      // Handle non-JSON response
      const text = await response.text();
      console.error("Unexpected response format:", text);
      document.getElementById("error_message").innerText =
        "Unexpected server response. Please try again.";
      document.getElementById("form_input_error_message").style.display =
        "flex";
    }
  } catch (error) {
    console.error("Error during login:", error);
    document.getElementById("error_message").innerText =
      "An error occurred during login. Please try again.";
    document.getElementById("form_input_error_message").style.display = "flex";
  }
}

// ##############################
// CUSTOMER_MESSAGES.HTML

// Manages sending messages from the customer side.
$(document).ready(function () {
  // Attaches a click event handler
  $("body").on("click", "#sendMessageButton", function () {
    console.log("Send button clicked");

    // Retrieves form data from the contact form
    var formData = new FormData($("#contactForm")[0]);

    // Sends an AJAX request to the server to send the message
    $.ajax({
      url: "/send_message",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // Log and display success message
        console.log("Success response:", response);
        $("#messageSent").text(response.info).show();
        $("#contactForm")[0].reset();

        // Hide the success message after 2 seconds
        setTimeout(function () {
          $("#messageSent").fadeOut();
        }, 2000);
      },
      // Callback function executed when the request fails
      error: function (xhr) {
        console.error("Error response:", xhr);
        var response = JSON.parse(xhr.responseText);
        alert("Der opstod en fejl: " + response.info);
      },
    });
  });
});

// ##############################
// ADMIN_MESSAGES.HTML
// Handles deleting messages from the admin interface.
function deleteMessage(button) {
  // Retrieve the message ID from the button's data attribute
  var messageId = button.getAttribute("data-message-id");
  console.log("Delete button clicked");
  console.log("Message ID:", messageId);

  // Send a DELETE request to the server to delete the message
  fetch("/delete_message", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "message_id=" + messageId,
  })
    .then((response) => {
      console.log("Response status:", response.status);
      return response.json();
    })
    .then((data) => {
      console.log("Response data:", data);
      // If the message was successfully deleted, remove it from the DOM
      if (data.info === "Message deleted.") {
        var messageBlock = button.closest(".message-block");
        if (messageBlock) {
          messageBlock.parentNode.removeChild(messageBlock);
          console.log("Message deleted successfully.");
        } else {
          console.log("Message block not found.");
        }
      } else {
        // If an error occurred, display an alert with the error message
        alert(data.info);
        console.log("Error:", data.info);
      }
    })
    .catch((error) => {
      console.error("Fetch error:", error);
    });
}

// ##############################
// ADMIN DELETE CLIPCARDS
// Handles deleting clipcards from the admin interface.
document.addEventListener("click", function (event) {
  if (event.target.classList.contains("delete-button")) {
    // Retrieve the clipcard ID from the data-clipcard-id attribute of the clicked button
    var clipcardId = event.target.getAttribute("data-clipcard-id");

    // Show a confirmation dialog before deleting
    var confirmDelete = confirm(
      "Er du sikker på, at du vil slette dette klippekort?"
    );

    if (confirmDelete) {
      deleteClipcard(clipcardId);
    } else {
      console.log("Sletning annulleret af brugeren.");
    }
  }
});

// Send a DELETE request to the server to delete the clipcard
function deleteClipcard(clipcardId) {
  fetch("/delete_clipcard/" + clipcardId, {
    method: "DELETE",
  })
    .then((response) => {
      if (response.ok) {
        // Find the clipcard element in the DOM and remove it
        var clipcardElement = document.getElementById("clipcard_" + clipcardId);
        if (clipcardElement) {
          clipcardElement.remove();
          console.log("Klippekort slettet.");
        } else {
          console.log("Klippekort element ikke fundet.");
        }
      } else {
        // If the request fails, throw an error
        throw new Error("Kunne ikke slette klippekortet.");
      }
    })
    .catch((error) => {
      console.error("Fejl:", error);
      alert("Der opstod en fejl ved sletning af klippekortet.");
    });
}

// ##############################
// ADMIN DELETE SUBSCRIPTIONS
document.addEventListener("click", function (event) {
  if (event.target.classList.contains("delete-subscription-button")) {
    // Retrieve the subscription ID from the data-subscription-id attribute
    var subscriptionId = event.target.getAttribute("data-subscription-id");

    // Show a confirmation dialog before deleting
    var confirmDelete = confirm(
      "Er du sikker på, at du vil slette dette abonnement?"
    );

    // Debugging: Log the confirmation result
    console.log("Confirm Delete:", confirmDelete);

    if (confirmDelete) {
      // Proceed with deletion if confirmed
      deleteSubscription(subscriptionId);
    } else {
      // Log message if deletion is canceled
      console.log("Sletning annulleret af brugeren.");
    }
  }
});

// Send a DELETE request to the server to delete the subscription
function deleteSubscription(subscriptionId) {
  const url = "/delete_subscription/" + subscriptionId;
  console.log("Sending DELETE request to:", url); // Log the URL being called

  fetch(url, {
    method: "DELETE", // Ensure method is DELETE
  })
    .then((response) => {
      console.log("Server response status:", response.status); // Log the response status
      if (response.status === 404) {
        throw new Error("Endpoint not found. Check server configuration.");
      }
      if (response.ok) {
        // Find the subscription element in the DOM and remove it
        var subscriptionElement = document.getElementById(
          "subscription_" + subscriptionId
        );
        if (subscriptionElement) {
          subscriptionElement.remove();
          console.log("Subscription element removed from the DOM."); // Log successful removal
        } else {
          console.log("Subscription element not found in the DOM."); // Log if element is not found
        }
      } else {
        // If the request fails, throw an error
        console.error(
          "Failed to delete subscription. Server returned:",
          response.statusText
        ); // Log the server's error message
        throw new Error("Kunne ikke slette abonnementet.");
      }
    })
    .catch((error) => {
      console.error("Fejl:", error); // Log the caught error
      alert("Der opstod en fejl ved sletning af abonnementet.");
    });
}

// ##############################
// TASKS
// Handles form submission for tasks
$(document).ready(function () {
  $("body").on("click", "#submitTaskButton", function () {
    console.log("Button clicked");

    // Validate the time form inputs
    var hours = $("#hours").val();
    var minutes = $("#minutes").val();

    if (hours === "" && minutes === "") {
      alert("Du skal udfylde mindst et af felterne i tidsregistrering");
      return false;
    }

    // Retrieve form data
    var formData = new FormData($("#taskForm")[0]);
    // Send an AJAX request to submit the task
    $.ajax({
      url: "/submit_task",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        // Log and display success message
        console.log("Success response:", response);
        $("#taskSubmissionMessage").text(response.info).show();
        $("#taskForm")[0].reset();

        // Hide the success message after 2 seconds
        setTimeout(function () {
          $("#taskSubmissionMessage").fadeOut();
        }, 2000);
      },
      error: function (xhr) {
        // Log and display error message if there's an error in the request
        console.error("Error response:", xhr);
        var response = JSON.parse(xhr.responseText);
        alert("Der opstod en fejl: " + response.info);
      },
    });
  });
});

// ##############################
// PASSWORD_FIELD.TPL

// Manages the visibility toggle for password fields.
$(document).ready(function () {
  // Attach a click event handler
  $("#visibility_button").on("click", function () {
    // Retrieve the password input field and visibility icons
    var input = $("#password_input");
    var icons = $(".visibility_icon");
    // Toggle the visibility of the password input field between text and password
    input.attr("type", input.attr("type") === "password" ? "text" : "password");
    // Toggle the visibility of visibility icons
    icons.toggleClass("object_hidden");
  });
});

// ##############################
// BURGERMENU
document.addEventListener("DOMContentLoaded", function () {
  var burgerButton = document.getElementById("icon_large");
  var mobileNav = document.getElementById("mobile-nav");

  if (burgerButton && mobileNav) {
    burgerButton.addEventListener("click", function () {
      mobileNav.classList.toggle("hidden");
    });
  } else {
    if (!burgerButton) {
      console.error("Burger menu button not found");
    }
    if (!mobileNav) {
      console.error("Mobile navigation element not found");
    }
  }
});

// ##############################
// ADMIN SETTINGS - DELETE USER
function deleteUser(button) {
  // Vis en bekræftelsesdialog
  var confirmDelete = confirm(
    "Er du sikker på, at du vil slette denne bruger?"
  );

  // Hvis brugeren bekræfter, fortsæt med sletningen
  if (confirmDelete) {
    // Retrieve the user ID from the button's data attribute
    var userId = button.getAttribute("data-user-id");
    console.log("Delete button clicked");
    console.log("User ID:", userId);

    // Send a DELETE request to the server to delete the user
    fetch("/delete_user", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: "user_id=" + userId,
    })
      .then((response) => {
        console.log("Response status:", response.status);
        return response.json();
      })
      .then((data) => {
        console.log("Response data:", data);
        // If the user was successfully deleted, remove the user block from the DOM
        if (data.info === "User deleted.") {
          var userBlock = button.closest(".customer-block");
          if (userBlock) {
            userBlock.parentNode.removeChild(userBlock);
            console.log("User deleted successfully.");
          } else {
            console.log("User block not found.");
          }
        } else {
          // If an error occurred, display an alert with the error message
          alert(data.info);
          console.log("Error:", data.info);
        }
      })
      .catch((error) => {
        console.error("Fetch error:", error);
      });
  } else {
    // Hvis brugeren annullerer, gør intet
    console.log("Sletning annulleret af brugeren.");
  }
}

// ##############################
// CUSTOMER SETTINGS - UPDATE PROFILE
$(document).ready(function () {
  $("body").on("click", "#updateProfileButton", function () {
    var formData = new FormData($("#update_profile_form")[0]);

    $.ajax({
      url: "/update_profile",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        console.log("Success response:", response);
        $("#message").text("Profil opdateret!").show();

        setTimeout(function () {
          $("#message").fadeOut();
        }, 2000);
      },
      error: function (xhr) {
        console.error("Error response:", xhr);
        var response = JSON.parse(xhr.responseText);
        alert("Der opstod en fejl: " + response.info);
      },
    });
  });
});

// ##############################
// CUSTOMER SETTINGS - DELETE PROFILE
$(document).ready(function () {
  $("body").on("click", "#deleteProfileButton", function () {
    var userId = $(this).data("user-id");

    // Vis en bekræftelsesdialog, før du fortsætter
    if (confirm("Er du sikker på, at du vil slette din profil?")) {
      $.ajax({
        url: "/delete_profile",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ user_id: userId }),
        success: function () {
          // Redirect to the homepage after successful deletion
          window.location.href = "/";
        },
        error: function (xhr) {
          // Handle the error here
          var responseText = xhr.responseText;
          alert("Der opstod en fejl: " + responseText);
        },
      });
    } else {
      // Log message if deletion is canceled
      console.log("Sletning annulleret af brugeren.");
    }
  });
});

// ##############################
// BUY CLIPCARD & SUBSCRIPTION
// Function to dynamically load Stripe.js
let stripe;

// Load Stripe.js dynamically
function loadStripeScript(callback) {
  if (typeof Stripe !== "undefined") {
    // Stripe.js is already loaded, execute the callback
    callback();
    return;
  }

  // Create a script element
  const script = document.createElement("script");
  script.src = "https://js.stripe.com/v3/";
  script.async = true;
  script.onload = () => {
    // Stripe.js has been loaded, execute the callback
    callback();
  };
  script.onerror = (error) => {
    console.error("Failed to load Stripe.js", error);
  };

  // Append the script to the document head
  document.head.appendChild(script);
}

// Initialize Stripe after Stripe.js is loaded
function initializeStripe() {
  // Check if Stripe.js is loaded
  if (typeof Stripe === "undefined") {
    console.error("Stripe.js is not loaded");
  } else {
    console.log("Stripe.js is loaded");

    // Initialize Stripe with your publishable key
    stripe = Stripe(
      "pk_live_51OlrinIT5aFkJJVMtRornGygVXxwrAaYQ257LxlxjyP0AspoONwJBN1sitgOzy7V1PjZJKAvIvcMWxT0HpBJ6ep100CwO34lQV"
    );

    // Add event listeners to buttons
    document.querySelectorAll("[data-clipcard-type]").forEach((button) => {
      button.addEventListener("click", () => handleBuyButtonClick(button));
    });
  }
}

// Function to handle buy button click
async function handleBuyButtonClick(button) {
  const clipcardType = button.getAttribute("data-clipcard-type");
  const clipcardPrice = button.getAttribute("data-clipcard-price");

  try {
    const response = await fetch("/create_checkout_session", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        clipcard_type: clipcardType,
        clipcard_price: clipcardPrice,
      }),
    });

    const session = await response.json();

    if (!session.id) {
      throw new Error("No session ID returned");
    }

    const result = await stripe.redirectToCheckout({
      sessionId: session.id,
    });
    if (result.error) {
      alert(result.error.message);
    }
  } catch (error) {
    console.error("Error:", error);
  }
}

// Load Stripe.js and initialize it
loadStripeScript(initializeStripe);

// Function to handle subscription button click
async function handleSubscriptionButtonClick(button) {
  const subscriptionType = button.getAttribute("data-subscription-type");
  const subscriptionPrice = button.getAttribute("data-subscription-price");

  try {
    const response = await fetch("/create_subscription_checkout_session", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        subscription_type: subscriptionType,
        subscription_price: subscriptionPrice,
      }),
    });

    const session = await response.json();

    if (!session.id) {
      throw new Error("No session ID returned");
    }

    const result = await stripe.redirectToCheckout({
      sessionId: session.id,
    });
    if (result.error) {
      alert(result.error.message);
    }
  } catch (error) {
    console.error("Error:", error);
  }
}

// Add event listeners to subscription buttons
document.querySelectorAll(".buy-button").forEach((button) => {
  button.addEventListener("click", () => handleSubscriptionButtonClick(button));
});

// ##############################
// CONTACT FORMULAR - SEND MAILS
$("#mailForm").submit(function (event) {
  event.preventDefault();

  var formData = new FormData(this);

  $.ajax({
    url: "/send-email",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      console.log("Success response:", response);
      $("#contactMessageSent").text(response.info).show();
      $("#mailForm")[0].reset();

      setTimeout(function () {
        $("#contactMessageSent").fadeOut();
      }, 2000);
    },
    error: function (xhr) {
      console.error("Error response:", xhr);
      var response = JSON.parse(xhr.responseText);
      alert("Der opstod en fejl: " + response.info);
    },
  });
});

// ##############################
// CONTACT FORMULAR - CANCEL SUBSCRIPTION MAILS
$(document).on("submit", "#cancelForm", function (event) {
  event.preventDefault();

  var formData = new FormData(this);

  $.ajax({
    url: "/cancel-subscription",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      console.log("Success response:", response);
      $("#cancelMessageSent").text(response.info).show();
      $("#cancelForm")[0].reset();

      setTimeout(function () {
        $("#cancelMessageSent").fadeOut();
      }, 6000);
    },
    error: function (xhr) {
      console.error("Error response:", xhr);
      var response = JSON.parse(xhr.responseText);
      alert("Der opstod en fejl: " + response.info);
    },
  });
});

// ##############################
// RESET AND UPDATE PASSWORD RESPONSE
document.addEventListener("DOMContentLoaded", function () {
  // Kode til formularen på /request_reset_password
  const resetForm = document.getElementById("resetForm");
  if (resetForm) {
    resetForm.addEventListener("submit", function (event) {
      event.preventDefault(); // Forhindrer standardformularindsendelse
      console.log("Reset form submission intercepted");

      // Hent email input
      const email = document.querySelector('input[name="email"]').value;

      // Sender AJAX-request med fetch API
      fetch("/request_reset_password", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: "email=" + encodeURIComponent(email),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.message) {
            // Hvis forespørgslen lykkes
            document.getElementById("resetCodeSent").style.display = "block";
            document.getElementById("resetCodeError").style.display = "none";
          } else if (data.error) {
            // Hvis serveren returnerer en fejl
            document.getElementById("resetCodeError").style.display = "block";
            document.getElementById("resetCodeSent").style.display = "none";
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          document.getElementById("resetCodeError").style.display = "block";
          document.getElementById("resetCodeSent").style.display = "none";
        });
    });
  }

  // Kode til formularen på /reset_password
  const passwordForm = document.getElementById("resetPasswordForm");
  if (passwordForm) {
    const passwordUpdateSuccess = document.getElementById(
      "passwordUpdateSuccess"
    );
    const passwordUpdateError = document.getElementById("passwordUpdateError");

    passwordForm.addEventListener("submit", function (event) {
      event.preventDefault();
      const formData = new FormData(passwordForm);

      fetch("/reset-password", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.message) {
            passwordUpdateSuccess.textContent = data.message;
            passwordUpdateSuccess.style.display = "block";
            passwordUpdateError.style.display = "none";
          } else if (data.error) {
            passwordUpdateError.textContent = data.error;
            passwordUpdateError.style.display = "block";
            passwordUpdateSuccess.style.display = "none";
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          passwordUpdateError.textContent =
            "Der opstod en fejl. Prøv venligst igen.";
          passwordUpdateError.style.display = "block";
          passwordUpdateSuccess.style.display = "none";
        });
    });
  }
});

// ##############################
// RESET AND UPDATE USERNAME RESPONSE
document.addEventListener("DOMContentLoaded", function () {
  // Håndtering af formularen for at anmode om nulstilling af brugernavn
  const requestUsernameResetForm = document.getElementById(
    "requestUsernameResetForm"
  );
  if (requestUsernameResetForm) {
    const usernameResetSuccess = document.getElementById(
      "usernameResetSuccess"
    );
    const usernameResetError = document.getElementById("usernameResetError");

    requestUsernameResetForm.addEventListener("submit", function (event) {
      event.preventDefault(); // Forhindrer standardformularindsendelse

      // Hent data fra formularen
      const formData = new FormData(requestUsernameResetForm);

      // Send AJAX-request med fetch API
      fetch("/request_reset_username", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.message) {
            // Hvis forespørgslen lykkes
            usernameResetSuccess.textContent = data.message;
            usernameResetSuccess.style.display = "block";
            usernameResetError.style.display = "none";
          } else if (data.error) {
            // Hvis serveren returnerer en fejl
            usernameResetError.textContent = data.error;
            usernameResetError.style.display = "block";
            usernameResetSuccess.style.display = "none";
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          usernameResetError.textContent =
            "Der opstod en fejl. Prøv venligst igen.";
          usernameResetError.style.display = "block";
          usernameResetSuccess.style.display = "none";
        });
    });
  }

  // Håndtering af formularen for at opdatere brugernavn
  const resetUsernameForm = document.getElementById("resetUsernameForm");
  if (resetUsernameForm) {
    const usernameUpdateSuccess = document.getElementById(
      "usernameUpdateSuccess"
    );
    const usernameUpdateError = document.getElementById("usernameUpdateError");

    resetUsernameForm.addEventListener("submit", function (event) {
      event.preventDefault(); // Forhindrer standardformularindsendelse

      // Hent data fra formularen
      const formData = new FormData(resetUsernameForm);

      // Send AJAX-request med fetch API
      fetch("/update_username", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.message) {
            // Hvis forespørgslen lykkes
            usernameUpdateSuccess.textContent = data.message;
            usernameUpdateSuccess.style.display = "block";
            usernameUpdateError.style.display = "none";
          } else if (data.error) {
            // Hvis serveren returnerer en fejl
            usernameUpdateError.textContent = data.error;
            usernameUpdateError.style.display = "block";
            usernameUpdateSuccess.style.display = "none";
          }
        })
        .catch((error) => {
          console.error("Error:", error);
          usernameUpdateError.textContent =
            "Der opstod en fejl. Prøv venligst igen.";
          usernameUpdateError.style.display = "block";
          usernameUpdateSuccess.style.display = "none";
        });
    });
  }
});
