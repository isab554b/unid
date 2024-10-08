<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{ profile_content["admin_specific_content"]["profile_admin_clipcard"]["decorative_header_text"] }}
    </p>
    <h2>
      <!-- prettier-ignore -->
      {{ profile_content["admin_specific_content"]["profile_admin_clipcard"]["header_text"] }}
    </h2>
  </div>
  <div class="grid lg:grid-cols-2 gap-8">
    <!-- prettier-ignore -->
    % if active_clipcards:
      % for clipcard in active_clipcards:
    <div id="clipcard_{{ clipcard['clipcard_id'] }}">
      <div id="content_box_styling">
        <div id="content_box_header_styling">
          <div
            class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
          >
            <div id="icon_medium" class="text-unidDarkBlue">
              % include(global_content['ui_icons']['card'])
            </div>
            <p class="font-bold text-lg text-unidDarkBlue">
              {{ clipcard["first_name"] }} {{ clipcard["last_name"] }}
            </p>
          </div>
        </div>
        <div class="flex flex-col gap-8 p-6 text-unidDarkBlue">
          <!-- USER -->
          <div class="space-y-2 text-sm">
            <div class="space-y-1">
              <p id="form_label">Brugeroplysninger</p>
              <hr />
            </div>
            <div class="space-y-2">
              <div class="flex gap-2">
                <p class="font-semibold">Navn:</p>
                <p>{{ clipcard["first_name"] }} {{ clipcard["last_name"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Brugernavn:</p>
                <p>{{ clipcard["username"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Telefon:</p>
                <p>{{ clipcard["phone"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Email:</p>
                <p>{{ clipcard["email"] }}</p>
              </div>
            </div>
          </div>
          <!-- WEBSITE -->
          <div class="space-y-2 text-sm">
            <div class="space-y-1">
              <p id="form_label">Website</p>
              <hr />
            </div>
            <div class="space-y-2">
              <div class="flex gap-2">
                <p class="font-semibold">Navn:</p>
                <p>{{ clipcard["website_name"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">URL:</p>
                <p>{{ clipcard["website_url"] }}</p>
              </div>
            </div>
          </div>
          <!-- CLIPCARD -->
          <div class="space-y-2 text-sm">
            <div class="space-y-1">
              <p id="form_label">Klippekortoplysninger</p>
              <hr />
            </div>
            <div class="space-y-2">
              <div class="gap-2">
                <p class="font-semibold">Klippekort ID:</p>
                <p>{{ clipcard["clipcard_id"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Klippekorttype:</p>
                <p>{{ clipcard["clipcard_type_title"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Købt den:</p>
                <p>{{ clipcard["formatted_created_at"] }}</p>
              </div>
            </div>
          </div>
          <!-- TIME -->
          <div class="space-y-2 text-sm">
            <div class="space-y-1">
              <p id="form_label">Timeoverblik</p>
              <hr />
            </div>
            <div class="space-y-2">
              <div class="flex gap-2">
                <p class="font-semibold">Tid brugt:</p>
                <p>{{ clipcard["time_used_text"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Tid tilbage:</p>
                <p>{{ clipcard["remaining_time_text"] }}</p>
              </div>
            </div>
          </div>
          <div class="w-full text-red-600">
            <div class="justify-end flex items-center">
              <button
                type="button"
                class="delete-button items-center flex gap-1.5 text-sm font-semibold"
                data-clipcard-id="{{ clipcard['clipcard_id'] }}"
              >
                <div id="icon_small">
                  % include(global_content['ui_icons']['trashcan'])
                </div>
                Slet
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- prettier-ignore -->
    % end 
      % else:
    <p class="text-sm">Ingen aktive klippekort.</p>
    % end
  </div>
</div>
