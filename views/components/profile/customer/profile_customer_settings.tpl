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
        <div
          id="content_box_header_styling"
          class="space-y-1 lg:space-y-0 lg:flex justify-between"
        >
          <div
            class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
          >
            <div id="icon_medium" class="fill-unidPurple">
              % include(global_content['ui_icons']['user'])
            </div>
            <p id="content_box_header_text">
              {{ user["first_name"] }} {{ user["last_name"] }}
            </p>
          </div>
        </div>
        <div class="flex flex-col p-6 text-unidPurple">
          <form id="update_profile_form">
            <div class="space-y-8 text-sm">
              <div class="space-y-2 text-sm">
                <div class="flex gap-2 items-center">
                  <p id="form_label">Brugernavn:</p>
                  <input
                    type="text"
                    name="username"
                    value="{{ user['username'] }}"
                    required
                  />
                </div>
                <hr />
                <div class="flex gap-2 items-center">
                  <p class="font-semibold">Telefon:</p>
                  <input
                    type="tel"
                    name="phone"
                    value="{{ user['phone'] }}"
                    required
                  />
                </div>

                <div class="space-y-2">
                  <div class="flex gap-2">
                    <p class="font-semibold">Email:</p>
                    <input
                      type="email"
                      name="email"
                      value="{{ user['email'] }}"
                      required
                    />
                  </div>
                </div>
              </div>
              <div class="w-full flex justify-between">
                <div>
                  <button
                    type="button"
                    id="updateProfileButton"
                    class="text-unidPurple items-center flex gap-1.5 text-sm font-semibold"
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
          <div id="message" class="text-unidPurple text-sm"></div>
        </div>
      </div>
    </div>
  </div>
</div>
