<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{profile_content["admin_specific_content"]["profile_admin_settings"]["decorative_header_text"]}}
    </p>
    <h2>
      <!-- prettier-ignore -->
      {{profile_content["admin_specific_content"]["profile_admin_settings"]["header_text"]}}
    </h2>
  </div>
  <div class="grid gap-8">
    <!-- prettier-ignore -->
    % if customers: 
      % for customer in customers:
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
              {{ customer["first_name"] }} {{ customer["last_name"] }}
            </p>
          </div>
        </div>
        <div class="flex flex-col gap-8 p-6 text-unidPurple">
          <div class="space-y-8 text-sm">
            <div class="space-y-2 text-sm">
              <div class="space-y-1">
                <div
                  class="lg:flex space-y-1 lg:space-y-0 justify-between items-center"
                >
                  <div class="flex gap-2 items-center">
                    <p id="form_label">Køb:</p>
                    <p class="text-base font-medium">
                      {{ customer["clipcard_type"] }}
                    </p>
                  </div>
                  <p class="font-medium">
                    {{ customer["website_name"] }}:
                    {{ customer["website_url"] }}
                  </p>
                </div>
                <hr />
              </div>
              <div class="space-y-2">
                <div class="flex gap-2">
                  <p class="font-semibold">Email:</p>
                  <p>{{ customer["email"] }}</p>
                </div>
                <div class="flex gap-2">
                  <p class="font-semibold">Telefon:</p>
                  <p>{{ customer["phone"] }}</p>
                </div>
              </div>
            </div>
            <div class="w-full flex justify-between">
              <div></div>
              <!-- Hvis du vil tilføje flere felter senere -->
              <div class="text-red-600">
                <div class="justify-end flex items-center">
                  <button
                    data-user-id="{{ customer['user_id'] }}"
                    onclick="deleteUser(this)"
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
          </div>
        </div>
      </div>
    </div>
    <!-- prettier-ignore -->
    % end 
    % else:
    <p class="text-sm">Ingen kunder at vise endnu.</p>
    % end
  </div>
</div>
