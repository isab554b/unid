<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_settings"]["decorative_header_text"] }}
    </p>
    <h2>
      <!-- prettier-ignore -->
      {{ profile_content["customer_specific_content"]["profile_customer_settings"]["header_text"] }}
    </h2>
  </div>
  <div class="grid gap-8">
    <div class="customer-block">
      <div id="content_box_styling">
        <div id="content_box_header_styling" class="">
          <div
            class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
          >
            <div id="icon_medium" class="text-unidDarkBlue">
              % include(global_content['ui_icons']['user'])
            </div>
            <p class="font-bold text-lg text-unidDarkBlue">
              {{ user["first_name"] }} {{ user["last_name"] }}
            </p>
          </div>
        </div>
        <div class="flex flex-col p-6 text-unidDarkBlue">
          <form id="update_profile_form">
            <div class="space-y-8 text-sm">
              <div class="space-y-4 text-sm">
                <div>
                  <label for="brugernavn" class="space-y-2">
                    <div class="flex space-between justify-between text-sm">
                      <p id="form_label" class="text-sm">Brugernavn</p>
                    </div>
                    <div class="w-full text-sm">
                      <input
                        id="second_form_input"
                        type="text"
                        name="username"
                        value="{{ user['username'] }}"
                        required
                      />
                    </div>
                  </label>
                </div>
                <div>
                  <label for="telefon" class="space-y-2">
                    <div class="flex space-between justify-between text-sm">
                      <p id="form_label" class="text-sm">Telefon</p>
                    </div>
                    <div class="w-full text-sm">
                      <input
                        id="second_form_input"
                        type="tel"
                        name="phone"
                        value="{{ user['phone'] }}"
                        required
                      />
                    </div>
                  </label>
                </div>
                <div>
                  <label for="email" class="space-y-2">
                    <div class="flex space-between justify-between text-sm">
                      <p id="form_label" class="text-sm">Email</p>
                    </div>
                    <div class="w-full text-sm">
                      <input
                        id="second_form_input"
                        type="email"
                        name="email"
                        value="{{ user['email'] }}"
                        required
                      />
                    </div>
                  </label>
                </div>
              </div>
              <div class="w-full flex justify-between">
                <div>
                  <button
                    type="button"
                    id="updateProfileButton"
                    class="text-unidDarkBlue items-center flex gap-1.5 text-sm font-semibold"
                  >
                    <div id="icon_small">
                      % include(global_content['ui_icons']['pen'])
                    </div>
                    Opdater profil
                  </button>
                </div>
                <div class="text-red-600">
                  <button
                    id="deleteProfileButton"
                    data-user-id="{{ user['user_id'] }}"
                    type="button"
                    class="items-center flex gap-1.5 text-sm font-semibold"
                  >
                    <div id="icon_small">
                      % include(global_content['ui_icons']['trashcan'])
                    </div>
                    Slet bruger
                  </button>
                </div>
              </div>
            </div>
          </form>
          <div class="text-unidDarkBlue mx-auto flex-col space-y-4 text-sm">
            <p id="message"></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
