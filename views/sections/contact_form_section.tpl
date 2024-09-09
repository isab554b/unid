<div
  class="grid grid-cols-1 lg:grid-cols-2 gap-6 lg:gap-16 justify-center items-center"
>
  <div class="w-2/3 flex items-center justify-center mx-auto">
    <img
      src="/assets/illustrations/{{ contact_content['illustration'] }}"
      alt="{{ contact_content['illustration_alt'] }}"
    />
  </div>
  <div
    class="bg-unidYellow order-first lg:order-last mx-auto flex flex-col w-full p-10 space-y-8 rounded-lg"
  >
    <div class="space-y-4">
      <h3>{{ contact_content["contact_form_section"]["header_text"] }}</h3>
      <p class="text-unidDarkBlue">
        {{ contact_content["contact_form_section"]["subheader_text"] }}
      </p>
    </div>
    <form id="mailForm" action="/send-email" method="post" class="space-y-4">
      <label for="full_name" class="space-y-1.5 block">
        <div class="flex space-between justify-between">
          <p id="form_label">Navn</p>
        </div>
        <div class="relative w-full">
          <div
            class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidBlue rounded-bl-md rounded-tl-md"
          >
            <div id="icon_small" class="fill-white text-white w-5 h-5">
              % include(global_content['ui_icons']['user_circle'])
            </div>
          </div>
          <div
            class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidBlue rounded-bl-md rounded-tl-md"
          >
            <div id="icon_small" class="fill-white text-white w-5 h-5">
              % include(global_content['ui_icons']['user_circle'])
            </div>
          </div>
          <input
            id="form_input"
            type="text"
            name="full_name"
            placeholder="Lorem Ipsum"
            required
          />
        </div>
      </label>
      <label for="email" class="space-y-1.5 block">
        <div class="flex space-between justify-between">
          <p id="form_label">Email</p>
        </div>
        <div class="relative w-full">
          <div
            class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidBlue rounded-bl-md rounded-tl-md"
          >
            <div id="icon_small" class="fill-white text-white w-5 h-5">
              % include(global_content['ui_icons']['email'])
            </div>
          </div>
          <div
            class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidBlue rounded-bl-md rounded-tl-md"
          >
            <div id="icon_small" class="fill-white text-white w-5 h-5">
              % include(global_content['ui_icons']['email'])
            </div>
          </div>
          <input
            id="form_input"
            type="email"
            name="email"
            placeholder="loremipsum@mail.dk"
            required
          />
        </div>
      </label>
      <label for="message" class="space-y-1.5 block">
        <div class="flex space-between justify-between">
          <p id="form_label">Besked</p>
        </div>
        <div class="relative w-full overflow-auto">
          <div
            class="absolute inset-y-0 start-0 flex items-center px-4 bg-unidBlue h-full rounded-bl-md rounded-tl-md"
          >
            <div id="icon_small" class="fill-white text-white w-5 h-5">
              % include(global_content['ui_icons']['message'])
            </div>
          </div>
          <textarea
            id="form_input"
            class="-mb-1.5"
            type="message"
            name="message"
            inputmode="text"
            placeholder="Lorem ipsum dolor sit amet..."
            required
          ></textarea>
        </div>
      </label>
      <button type="submit" id="primary_button" class="contact-submit-button">
        Send besked
      </button>
    </form>
    <p
      id="contactMessageSent"
      style="display: none"
      class="text-unidDarkBlue text-sm"
    ></p>
  </div>
</div>
