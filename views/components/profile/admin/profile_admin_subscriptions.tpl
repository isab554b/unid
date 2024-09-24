<div class="space-y-8">
  <div class="space-y-2">
    <p id="decorative_header">
      <!-- prettier-ignore -->
      {{ profile_content["admin_specific_content"]["profile_admin_subscriptions"]["decorative_header_text"] }}
    </p>
    <h2>
      <!-- prettier-ignore -->
      {{ profile_content["admin_specific_content"]["profile_admin_subscriptions"]["header_text"] }}
    </h2>
  </div>
  <div class="grid lg:grid-cols-2 gap-8">
    <!-- prettier-ignore -->
    % if active_subscriptions:
    % for subscription in active_subscriptions:
    <div id="subscription_{{ subscription['subscription_id'] }}">
      <div id="content_box_styling">
        <div id="content_box_header_styling">
          <div
            class="flex md:flex-col lg:flex-row gap-4 md:gap-2 lg:gap-4 items-center justify-center"
          >
            <div id="icon_medium" class="text-unidDarkBlue">
              % include(global_content['ui_icons']['cart'])
            </div>
            <p class="font-bold text-lg text-unidDarkBlue">
              {{ subscription["first_name"] }} {{ subscription["last_name"] }}
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
                <p>
                  {{ subscription["first_name"] }}
                  {{ subscription["last_name"] }}
                </p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Brugernavn:</p>
                <p>{{ subscription["username"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Telefon:</p>
                <p>{{ subscription["phone"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Email:</p>
                <p>{{ subscription["email"] }}</p>
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
                <p>{{ subscription["website_name"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">URL:</p>
                <p>{{ subscription["website_url"] }}</p>
              </div>
            </div>
          </div>
          <!-- CLIPCARD -->
          <div class="space-y-2 text-sm">
            <div class="space-y-1">
              <p id="form_label">Abonnementsoplysninger</p>
              <hr />
            </div>
            <div class="space-y-2">
              <div class="gap-2">
                <p class="font-semibold">Abonnement ID:</p>
                <p>{{ subscription["subscription_id"] }}</p>
              </div>
              <div class="flex gap-2">
                <p class="font-semibold">Købt den:</p>
                <p>{{ subscription["formatted_created_at"] }}</p>
              </div>
            </div>
          </div>
          <div class="w-full text-red-600">
            <div class="justify-end flex items-center">
              <button
                type="button"
                class="delete-subscription-button items-center flex gap-1.5 text-sm font-semibold"
                data-subscription-id="{{ subscription['subscription_id'] }}"
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
    <p class="text-sm">Ingen aktive abonnementer.</p>
    % end
  </div>
</div>
